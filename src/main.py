import os
from dotenv import load_dotenv
from src.core.agent import AgentCore
from src.providers.slack_provider import SlackProvider

def main():
    # Load environment variables
    load_dotenv()

    # Initialize the AI Brain
    agent = AgentCore()
    
    # Initialize the Provider (Slack in this case)
    bot = SlackProvider(agent)

    # Check for tokens before starting
    if not os.environ.get("SLACK_BOT_TOKEN") or not os.environ.get("SLACK_APP_TOKEN"):
        print("CRITICAL ERROR: SLACK_BOT_TOKEN or SLACK_APP_TOKEN is missing in .env")
        return

    # Start the bot
    try:
        print("Starting bot...")
        bot.start()
    except Exception as e:
        print(f"Error starting the bot: {e}")

if __name__ == "__main__":
    main()

