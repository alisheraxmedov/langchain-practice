from assistant.core.llm import llm
from assistant.core.prompts import prompt
from assistant.services.generator import GeneratorService



def assistant():
    generator = GeneratorService(llm=llm, prompt=prompt)
    
    text = "I have email text for my friends, can you make it more professional?"
    result = generator.generate_response(text=text)

    print(result)
