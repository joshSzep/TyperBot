"""Command-line interface for TyperBot."""

import asyncio
import os
from typing import Annotated

import typer
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.text import Text

from typerbot.chat import ChatBot

app = typer.Typer(
    name="typerbot",
    help="A terminal-based chatbot using Claude AI.",
    add_completion=False,
)
console = Console()


@app.command()
def chat(
    api_key: Annotated[
        str | None,
        typer.Option(
            "--api-key",
            "-k",
            help="Anthropic API key. If not provided, will try ANTHROPIC_API_KEY env var.",
        ),
    ] = None,
    model: Annotated[
        str,
        typer.Option(
            "--model",
            "-m",
            help="Model to use for chat completion.",
        ),
    ] = "claude-3-opus-20240229",
) -> None:
    """Start an interactive chat session with the bot."""
    api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print(
            "[red]Error:[/red] No API key provided. Either pass --api-key or set ANTHROPIC_API_KEY environment variable.",
        )
        raise typer.Exit(1)

    bot = ChatBot(api_key=api_key, model=model)
    console.print(
        "[bold blue]TyperBot[/bold blue] - Type 'exit' or press Ctrl+C to quit\n",
    )

    async def chat_loop() -> None:
        while True:
            try:
                message = input("You: ")
                if message.lower() in ["exit", "quit"]:
                    break

                with Live(
                    Text("Thinking..."),
                    console=console,
                    refresh_per_second=4,
                ) as live:
                    response = await bot.chat(message)
                    live.update(Markdown(response))

                console.print()  # Add newline after response

            except KeyboardInterrupt:
                console.print("\nGoodbye! 👋")
                break
            except Exception as e:
                console.print(f"[red]Error:[/red] {str(e)}")
                break

    try:
        asyncio.run(chat_loop())
    except KeyboardInterrupt:
        console.print("\nGoodbye! 👋")


def main() -> None:
    """Entry point for the CLI."""
    app()
