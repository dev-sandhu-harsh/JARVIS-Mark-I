from jarvis.core.memory.utils.scoring import memory_importance

def write_facts(memory, facts: list[dict]):
    for fact in facts:
        memory.add(
            fact["text"],
            importance=memory_importance(fact["text"])
        )
