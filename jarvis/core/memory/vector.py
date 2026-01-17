import faiss
import json
import time
import math
from pathlib import Path
from sentence_transformers import SentenceTransformer
from jarvis.core.memory.base import Memory
from jarvis.core.memory.utils.scoring import recency_score, total_score


class VectorMemory(Memory):
    def __init__(self, path="model_memory/vector_memory.json"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.path.write_text(json.dumps({"items": []}))

        data = json.loads(self.path.read_text())
        self.items = data["items"]

        self.index = faiss.IndexFlatL2(384)
        if self.items:
            embeddings = self.model.encode([item["text"] for item in self.items])
            self.index.add(embeddings)

    # ---------- persistence ----------
    def _persist(self):
        self.path.write_text(json.dumps({"items": self.items}, indent=2))

    def _rebuild_index(self, items):
        self.items = items
        self.index.reset()
        if items:
            embeddings = self.model.encode([item["text"] for item in items])
            self.index.add(embeddings)
        self._persist()

    # ---------- write ----------
    def add(self, text: str, importance: float = 1.0):
        item = {
            "text": text,
            "importance": importance,
            "created_at": time.time()
        }

        embedding = self.model.encode([text])
        self.index.add(embedding)
        self.items.append(item)
        self._persist()

    # ---------- read ----------
    def search(self, query: str, k: int = 5):
        if not self.items:
            return []

        q_emb = self.model.encode([query])
        distances, indices = self.index.search(q_emb, min(len(self.items), 20))

        scored = []
        for d, i in zip(distances[0], indices[0]):
            item = self.items[i]
            similarity = 1 / (1 + d)
            recency = recency_score(item["created_at"])
            score = total_score(similarity, item["importance"], recency)
            scored.append((score, item["text"]))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [text for _, text in scored[:k]]

    # ---------- forgetting ----------
    def prune(self, min_score: float = 0.2):
        kept = []
        for item in self.items:
            r = recency_score(item["created_at"])
            if item["importance"] * r >= min_score:
                kept.append(item)

        self._rebuild_index(kept)