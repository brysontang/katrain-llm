import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class LLMInterface:
    def __init__(self):
        # Initialize your LLM client here
        # Example with OpenAI:
        from openai import OpenAI
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=openai_api_key)
        pass
        
    def get_response(self, prompt: str) -> str:
        # Implement your LLM call here
        # Example with OpenAI:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
        pass