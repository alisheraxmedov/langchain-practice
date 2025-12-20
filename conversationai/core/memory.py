from langchain_classic.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory,
)

from conversationai.config.settings import settings
from conversationai.core.llm import llm


class MemoryManager:
    def __init__(self):
        self.sessions = {}

    def _create_memory(self):
        
        memory_type = settings.MEMORY_TYPE.lower()

        if(memory_type == "buffer"):
            return ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True,
            )
        elif(memory_type == "window"):
            return ConversationBufferWindowMemory(
                memory_key="chat_history",
                return_messages=True,
                window_size=settings.WINDOW_SIZE,
            )
        elif(memory_type == "summary"):
            return ConversationSummaryMemory(
                llm=llm,
                memory_key="chat_history",
                return_messages=True,
            )
        else:
            raise ValueError(f"Unknown memory type: {memory_type}")


    def get_memory(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = self._create_memory()
        
        return self.sessions[session_id]

    def clear_memory(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

memory_manager = MemoryManager()