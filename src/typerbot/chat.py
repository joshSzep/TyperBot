"""Chat functionality for TyperBot using LangChain and Anthropic."""

from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain.schema.messages import BaseMessage
from langchain_anthropic import ChatAnthropic
from rich.console import Console

console = Console()


class ChatBot:
    """A chatbot powered by Anthropic's Claude via LangChain."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "claude-3-opus-20240229",
    ) -> None:
        """Initialize the chatbot.

        Args:
            api_key: Anthropic API key. If None, will try to get from environment.
            model: The model to use for chat completion.
        """
        self.chat_model = ChatAnthropic(
            anthropic_api_key=api_key,  # type: ignore
            model=model,  # type: ignore
            max_tokens=1024,  # type: ignore
            temperature=0.7,
        )
        self.messages: list[BaseMessage] = []
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant. Be concise and clear in your responses.",
                ),
            ],
        )

    async def chat(self, message: str) -> str:
        """Chat with the bot and get the full response.

        Args:
            message: The user's message to the bot.

        Returns:
            The bot's complete response.
        """
        self.messages.append(HumanMessage(content=message))
        response = await self.chat_model.ainvoke(self.messages)
        self.messages.append(response)
        return str(response.content)

    def reset(self) -> None:
        """Reset the conversation history."""
        self.messages.clear()
