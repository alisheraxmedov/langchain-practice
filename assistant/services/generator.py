from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

class GeneratorService:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt
        self.chain: Runnable = self.prompt | self.llm | StrOutputParser()

    def generate_response(self, text: str) -> str:
        result = self.chain.invoke({"text": text})

        return result