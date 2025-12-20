from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SMART_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. You are given a question and you need to generate a response based on the memory."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

prompt = SMART_PROMPT_TEMPLATE
