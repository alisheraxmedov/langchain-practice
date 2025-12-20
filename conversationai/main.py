from conversationai.services.agent_logic import get_agent_executor


def conversationai():
    session_id = "session_1"
    agent_executor = get_agent_executor(session_id)
    
    while True:
        user_input = input("User: ") 
        response = agent_executor.invoke({"input": user_input})
        print("Assistant:", response["output"])