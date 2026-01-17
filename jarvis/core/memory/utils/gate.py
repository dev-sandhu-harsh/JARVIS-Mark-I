def allow_fact(fact: dict) -> bool:
    text = fact.get("text", "")
    confidence = fact.get("confidence", 0)

    if confidence < 0.7:
        return False

    if len(text) > 200:
        return False

    if text.endswith("?"):
        return False

    return True
