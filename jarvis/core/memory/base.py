from abc import ABC, abstractmethod
from typing import List

class Memory(ABC):

    @abstractmethod
    def add(self, text: str):
        pass

    @abstractmethod
    def search(self, query: str, k: int = 3) -> List[str]:
        pass

    @abstractmethod
    def prune(self, min_score = 0.2):
        pass
