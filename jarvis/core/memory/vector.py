import faiss
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from jarvis.core.memory.base import Memory

class VectorMemory(Memory):
    def __init__(self, path="model_memory/vector_memory.json"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.path = Path(path)
        self.path.parent.mkdir(parents = True, exist_ok = True)

        if not self.path.exists():
            self.path.write_text(json.dumps({"texts": []}))
        
        data = json.loads(self.path.read_text())
        self.texts = data["texts"]

        self.index = faiss.IndexFlatL2(384)
        if self.texts:
            embeddings = self.model.encode(self.texts)
            self.index.add(embeddings)
    
    def add(self, text:str):
        embedding = self.model.encode([text])
        self.index.add(embedding)

        self.texts.append(text)
        self.path.write_text(json.dumps({"texts": self.texts}, indent=2))

    def search(self, query:str, k: int = 3):
        if not self.texts:
            return []
        
        embedding = self.model.encode([query])
        _, indices = self.index.search(embedding, k)
        return [self.texts[i] for i in indices[0] if i < len(self.texts)]