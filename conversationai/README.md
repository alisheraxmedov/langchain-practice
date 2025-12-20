# Conversation AI Agent 🤖

A sophisticated conversational agent capable of using tools and maintaining context, powered by **Google Gemini** and **LangChain**.

## 🚀 Features

- **Tool-Using Agent**: Intelligently decides when to use external tools (e.g., searching orders, checking user info) to answer queries.
- **Context Awareness**: Maintains conversation history using customizable memory modules (Buffer, Window, Summary).
- **Smart Logic**: Uses LangChain's ReAct agent pattern for reasoning and acting.

## 📂 Project Structure

Organized for modularity and extendability.

```text
conversationai/
├── config/           # Configuration and environment settings
│   └── settings.py
├── core/             # Core AI components
│   ├── llm.py        # Gemini LLM configuration
│   ├── memory.py     # Memory management (Classic Memory)
│   └── prompts.py    # System prompts and templates
├── services/         # Business logic and tools
│   ├── agent_logic.py # Agent Executor assembly
│   ├── parsers.py    # Data structures (Pydantic models)
│   └── tools.py      # Custom tools (Order Search, User Info)
├── main.py           # Entry point
```

## 🛠️ Stack

- **Python 3.12+**
- **LangChain Classic** (Agents & Memory)
- **Google Gemini Pro** (LLM)
- **Pydantic** (Data Validation)
