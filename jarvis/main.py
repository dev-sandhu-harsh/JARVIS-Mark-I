import typer
from rich import print
from rich.console import Console
from jarvis.logger import setup_logger
from jarvis.orchestrator import Orchestrator

app = typer.Typer()
console = Console()
orchestrator = Orchestrator()

@app.command()
def main():
    setup_logger()
    print("[green]JARVIS online[/green]")

@app.command()
def ask(message: str, stream: bool = True):
    response = orchestrator.run(message)
    print(response)
    # kind, result = orchestrator.route(message)

    # if(kind == "tool"):
    #     print(result)
    #     return
    
    # if stream:
    #     for token in orchestrator.stream(message):
    #         console.print(token, end="", soft_wrap=True)
    #     console.print()
    # else:
    #     response = orchestrator.handle(message)
    #     print(response)


if __name__ == "__main__":
    app()