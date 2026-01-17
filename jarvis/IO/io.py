from abc import ABC, abstractmethod

class InputInterface(ABC):
    @abstractmethod
    def get_text(self) -> str:
        pass

class OutputInterface(ABC):
    @abstractmethod
    def output_text(self, text: str):
        pass
