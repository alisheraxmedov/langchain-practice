# Smart Prompt Assistant 🧠

A streamlined AI tool designed to transform raw input text into structured, professional outputs using **Google Gemini** and **LangChain**.

## 🚀 Features

- **Professional Email Generator**: Converts informal notes into polished, formal emails with subject lines.
- **Technical Explainer**: Breaks down complex concepts or analyzes the logical structure of non-technical text.
- **Instant Summaries (TL;DR)**: Provides concise 1-3 sentence summaries for quick reading.

## 📂 Project Structure

Designed with a modular "Clean Code" architecture for scalability.

```text
assistant/
├── config/           # Configuration management (Pydantic settings)
│   └── settings.py
├── core/             # Core AI components
│   ├── llm.py        # Gemini implementation
│   └── prompts.py    # Specialized PromptTemplates
├── services/         # Business logic
│   └── generator.py  # LCEL Chains & Generation logic
├── main.py           # CLI Entry point
```

## 🛠️ Stack

- **Python 3.10+**
- **LangChain** (Orchestration)
- **Google Gemini Pro** (LLM)
- **Pydantic** (Validation)
