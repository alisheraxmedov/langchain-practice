from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from conversationai.core.llm import llm
from conversationai.core.prompts import prompt
from conversationai.core.memory import memory_manager
from conversationai.services.tools import search_order, get_user_info

def get_agent_executor(session_id: str) -> AgentExecutor:
    # 1. Define tools
    tools = [search_order, get_user_info]

    # 2. Create the agent with tools bound to LLM
    agent = create_tool_calling_agent(llm, tools, prompt)

    # 3. Get session-specific memory
    memory = memory_manager.get_memory(session_id)

    # 4. Create Agent Executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )

    return agent_executor
