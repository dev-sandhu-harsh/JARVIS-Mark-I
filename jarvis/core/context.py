from pathlib import Path

def list_readable_files(root: str = "."):
    files = []
    for p in Path(root).glob("**/*.txt"):
        files.append(str(p))
    return files
