import json
from pydantic import ValidationError
from jarvis.core.ollama_llm import OLLAMA_LLM
from jarvis.core.tools.registry import TOOLS
from jarvis.core.tools.schema import ToolCall
from jarvis.core.json_utils import extract_json
from jarvis.core.memory.vector import VectorMemory
from jarvis.core.memory.utils.scoring import memory_importance
from jarvis.core.memory.utils.proposer import propose_facts
from jarvis.core.memory.utils.gate import allow_fact
from jarvis.core.memory.utils.writer import write_facts

class Orchestrator:
    def __init__(self):
        self.llm = OLLAMA_LLM()
        self.memory = VectorMemory()

    def route(self, user_input: str):
        data = extract_json(user_input)
        if not data:
            return ("llm", None)
        if "tool" not in data:
            return ("llm", None)
        
        try:
            tool_call = ToolCall(**data)

            tool = TOOLS.get(tool_call.tool)
            if not tool:
                return ("error", f"Unknown tool: {tool_call.tool}")
            
            result = tool.run(tool_call.args)
            return ("tool", result)
        
        except ValidationError:
            # JSON existed but was not a valid tool call
            return ("llm", None)

        except Exception as e:
            return ("error", str(e))
    
    def handle(self, user_input: str) -> str:
        return self.llm.generate(user_input)
    
    def stream(self, user_input: str):
        return self.llm.stream(user_input)
    
    def run(self, user_input: str):
        context = f"User request:\n{user_input}"

        self.memory.prune()
        memories = self.memory.search(user_input)

        if memories:
            context = (
                       "SYSTEM FACTS (always true):\n"
                        + "\n".join(memories)
                        + "\n\n"
                        + context
                    )
        
        for _ in range(5):
            response = self.llm.generate(context)

            kind, result = self.route(response)

            if kind == "tool":
                context += f"\n Tool result:\n{result}\n"
                continue

            if kind == "error":
                context += f"\nError:\n{result}\n"
                return result
            
            candidates = propose_facts(self.llm, user_input)
            approved = [
                fact for fact in candidates
                if allow_fact(fact)
            ]
            write_facts(self.memory, approved)

            return response
        
        return "Max steps reached."
