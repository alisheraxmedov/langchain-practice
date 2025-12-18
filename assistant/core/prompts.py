from langchain_core.prompts import PromptTemplate

SMART_PROMPT_TEMPLATE = """
As a high-level intelligent assistant, analyze the following text and provide a response in three distinct sections:

1. Professional Email
Write a formal and professional email based on this content. Suggest a subject line.

2. Technical Explanation
Explain the main ideas, technical terms, and logic in simple but professional language. If the text is not technical, analyze its logical structure.

3. Summary (TL;DR)
A concise summary of the most important points in 1-3 sentences.

INPUT TEXT:
{text}
"""

prompt = PromptTemplate.from_template(SMART_PROMPT_TEMPLATE)
