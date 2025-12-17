# Slack Agent with RAG

A modular Slack bot built with Python, LangChain, and OpenAI. It includes a simple RAG (Retrieval-Augmented Generation) system for domain-specific knowledge.

## Project Structure

- `src/core/`: The AI logic using LangChain and OpenAI.
- `src/rag/`: Vector store management for domain-specific questions.
- `src/providers/`: Modular messaging providers (currently supports Slack).
- `data/`: Put your `.txt` files here to feed the RAG system.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   - Copy `environment.example` to `.env`.
   - Fill in your `OPENAI_API_KEY`.
   - Fill in your Slack tokens (`SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN`).

3. Add knowledge:
   - Place any `.txt` files with domain-specific information into the `data/` folder.

4. (Optional) Pre-index data:
   - If you have many files, you can index them once so the bot starts instantly:
   ```bash
   python scripts/ingest_data.py
   ```

5. Run the bot:
   ```bash
   python -m src.main
   ```

## Slack Configuration

- Create an app at [api.slack.com/apps](https://api.slack.com/apps).
- Enable **Socket Mode**.
- Under **Slash Commands** or **Event Subscriptions**, subscribe to `app_mention` and `message.im`.
- Ensure your bot has `app_mentions:read` and `im:history` scopes (and `chat:write` to reply).

## Adding New Providers

To add a new provider (e.g., Microsoft Teams):
1. Create a new file in `src/providers/teams_provider.py`.
2. Inherit from `BaseProvider`.
3. Implement `start` and `send_message`.
4. Update `src/main.py` to use your new provider.

