# Agent Core

An autonomous AI agent that reasons about which tools to use to answer questions. Built to learn agentic AI from first principles.

## What It Does

- Answers questions by using tools (weather search, web search)
- Remembers conversation history
- Tracks API usage to avoid overspending
- Handles errors gracefully

## Setup

1. Clone the repo
2. Create `.env` with your OpenAI API key:
```
   OPENAI_API_KEY=your_key_here
```
3. Install dependencies:
```
   pip install -r requirements.txt
```
4. Run it:
```
   python main.py
```

## How It Works

You ask a question → Agent thinks if it needs tools → Agent calls tools → Agent answers based on tool results.

Example:
- You: "What's the weather in Delhi tomorrow?"
- Agent: Calls weather tool, gets data, tells you the weather