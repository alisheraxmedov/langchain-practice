# LangChain Practice Hub 🦜🔗

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)
![Manager](https://img.shields.io/badge/Dependency-uv-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

This repository serves as a collection of mini-projects designed to master **LangChain** concepts, ranging from basic prompts to advanced chains and agents. Each module focuses on specific real-world applications and "Clean Code" practices.

## 📂 Active Modules

| Project | Description | Documentation |
|---------|-------------|---------------|
| **Smart Assistant** | High-level text analysis tool (Email, Tech Explainer, Summary) using Gemini Pro. | [Read Docs](assistant/README.md) |
| **Conversation AI** | Stateful agent with memory and tools (Order Search, User Info) powered by ReAct logic. | [Read Docs](conversationai/README.md) |

---

## ⚡ Quick Start

This project uses **[uv](https://github.com/astral-sh/uv)** for blazing fast dependency management. We do not use `pip` or `poetry`.

### 1. Pre-requisites
Ensure you have `uv` installed:
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Installation
Clone the repo and sync dependencies:
```bash
# Install dependencies & create virtualenv automatically
uv sync
```

### 3. Environment Setup 🔐
You need to configure your API keys before running any project.

1.  Copy the example configuration:
    ```bash
    cp .env.example .env
    ```

2.  Open `.env` and fill in the required variables:
    ```ini
    # .env
    GOOGLE_API_KEY=AIzaSy...     # Get this from Google AI Studio
    GOOGLE_API_MODEL=gemini-pro  # Model version
    TEMPERATURE=0.7              # Creativity (0.0 - 1.0)
    ```

### 4. Running Projects 🚀
Run any script using `uv run`. It automatically handles environment activation.

```bash
# Run the main application
uv run app.py
```

---

## 📚 Educational Purpose
The code within this repository is structured for **educational clarity**:
- **Separation of Concerns**: Config, Core, Services are isolated.
- **Modern Python**: Uses Pydantic, Type Hinting, and LCEL.
- **Production Ready**: Concepts can be adapted for real-world deployment.

## 📄 License
This project is open-source and available under the terms of the [MIT License](LICENSE).
