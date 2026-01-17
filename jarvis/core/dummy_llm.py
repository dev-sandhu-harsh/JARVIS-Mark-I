from jarvis.core.llm import LLM

class Dummy_LLM(LLM):

    def generate(self, prompt: str) -> str:
        return f"ECHO: {prompt}"
    
    def stream(self, prompt: str) -> Iterable[str]:
        for word in prompt.split():
            yield word + " "