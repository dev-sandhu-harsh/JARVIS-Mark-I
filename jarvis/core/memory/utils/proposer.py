import json
from jarvis.core.json_utils import extract_json

PROMPT = """
Extract long-term user facts from the message.

Rules:
- Only stable, personal facts.
- No questions.
- No temporary states.
- No plans or tasks.
- Do not invent facts.
- If none, return empty list.
- JSON only.

Message:
"{message}"

Format:
{{
  "facts": [
    {{
      "text": "...",
      "type": "...",
      "confidence": 0.0
    }}
  ]
}}
"""

def propose_facts(llm, user_input: str) -> list[dict]:
    response = llm.generate(
        PROMPT.format(message=user_input)
    )
    try:
        data = extract_json(response)
        if not data:
            return []
        if "facts" not in data:
            return []
        return data.get("facts", [])
    except Exception:
        return []
