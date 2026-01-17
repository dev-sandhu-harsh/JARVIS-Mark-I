import time
import math

def recency_score(ts, half_life_days=30):
    age_days = (time.time() - ts) / 86400
    return math.exp(-age_days / half_life_days)

def total_score(similarity, importance, recency):
    return similarity * importance * recency

def memory_importance(text: str) -> float:
    if text.startswith("User name"):
        return 2.0
    if "preference" in text.lower():
        return 1.5
    return 0.5
