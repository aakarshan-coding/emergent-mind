"""Core value types shared across modules."""

from dataclasses import dataclass
from typing import NewType

AgentId = NewType("AgentId", str)


@dataclass(frozen=True)
class Message:
    """A message sent between agents. A recipient of None means broadcast."""

    sender: AgentId
    recipient: AgentId | None
    content: str
    step: int

    def is_for(self, agent: AgentId) -> bool:
        if agent == self.sender:
            return False
        return self.recipient is None or self.recipient == agent
