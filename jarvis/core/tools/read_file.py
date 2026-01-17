from jarvis.core.tools.base import Tool

class ReadFileTool(Tool):
    name = "read_file"
    description = "Read a text file from disk"

    def run(self, params):
        path = params.get("path")
        if not path:
            raise ValueError("path is required")
        
        with open(path, "r") as f:
            return f.read()