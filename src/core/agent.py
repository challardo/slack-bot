from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.rag.store import RAGSystem

class AgentCore:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.rag = RAGSystem()
        self.agent_executor = None

    def setup(self):
        """
        Sets up the Agent with a retrieval tool as described in the documentation.
        """
        retriever = self.rag.get_retriever()

        @tool
        def retrieve_knowledge(query: str) -> str:
            """
            Search the knowledge base for domain-specific information.
            Use this when you need facts about the company or technical details.
            """
            docs = retriever.invoke(query)
            return "\n\n".join([doc.page_content for doc in docs])

        tools = [retrieve_knowledge]
        
        # Modern prompt for a tool-calling agent
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful Slack assistant. Use the retrieve_knowledge tool to answer questions based on the knowledge base. If you don't know the answer, say you don't know."),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        # Create the agent using the modern tools API
        agent = create_openai_tools_agent(self.llm, tools, prompt)
        
        # Wrap in AgentExecutor
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            handle_parsing_errors=True
        )

    def ask(self, query: str) -> str:
        """
        Processes a query through the RAG agent.
        """
        if not self.agent_executor:
            self.setup()
        
        # The executor uses 'input' as the key and returns 'output'
        response = self.agent_executor.invoke({"input": query})
        return response["output"]

