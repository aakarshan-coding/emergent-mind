"""Backend-agnostic LLM interface. Concrete backends are chosen later."""

from dataclasses import dataclass
from typing import Literal, Protocol

Role = Literal["system", "user", "assistant"]


@dataclass(frozen=True)
class ChatMessage:
    role: Role
    content: str


class LLMClient(Protocol):
    def complete(self, messages: list[ChatMessage]) -> str: ...


class ScriptedClient:
    """Returns canned replies in order. For tests and dry runs."""

    def __init__(self, replies: list[str]) -> None:
        self._replies = list(replies)
        self.calls: list[list[ChatMessage]] = []

    def complete(self, messages: list[ChatMessage]) -> str:
        self.calls.append(list(messages))
        if not self._replies:
            raise RuntimeError("ScriptedClient ran out of replies")
        return self._replies.pop(0)
