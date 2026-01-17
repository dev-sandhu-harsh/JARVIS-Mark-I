import ollama
from jarvis.core.llm import LLM
from jarvis.core.prompts import SYSTEM_PROMPT

class OLLAMA_LLM(LLM):
    def __init__(self, model: str ="phi3:mini"):
        self.model = model
    
    def generate(self, prompt: str) -> str:
        response = ollama.generate(
            model = self.model,
            prompt = prompt,
            system = SYSTEM_PROMPT
        )
        return response["response"]
    
    def stream(self, prompt: str) -> Iterable[str]:
        for chunk in ollama.generate(
            model = self.model,
            prompt = prompt,
            system = SYSTEM_PROMPT,
            stream = True
        ):
            yield chunk["response"]