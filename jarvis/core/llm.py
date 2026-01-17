from abc import ABC, abstractmethod
from typing import Iterable

class LLM(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
    
    @abstractmethod
    def stream(self, prompt: str) -> Iterable[str]:
        pass
    