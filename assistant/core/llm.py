from langchain_google_genai.llms import ChatGoogleGenerativeAI
from assistant.config.settings import settings

def get_llm(temperature: float = 0.7):
    return ChatGoogleGenerativeAI(
        api_key=settings.GEMINI_API_KEY,
        model=settings.GEMINI_MODEL,
        temperature=temperature,
    )

llm = get_llm()
