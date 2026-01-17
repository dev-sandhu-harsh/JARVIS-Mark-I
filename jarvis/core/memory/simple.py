import json
from pathlib import Path
from jarvis.core.memory.base import Memory

class SimpleMemory(Memory):
    def __init__(self, path: str = "memory.json"):
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("[]")
        
    def add(self, text: str):
        data = json.loads(self.path.read_text())
        data.append(text)
        self.path.write_text(json.dumps(data, indent = 2))
    
    def search(self, query: str, k: int = 3):
        data = json.loads(self.path.read_text())
        return data[-k:]
        