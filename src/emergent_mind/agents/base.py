from dataclasses import dataclass, field
from typing import Any, Protocol

from emergent_mind.types import AgentId, Message


@dataclass(frozen=True)
class Observation:
    """What one agent perceives at a step: its partial view plus delivered messages."""

    agent: AgentId
    step: int
    view: dict[str, Any]
    inbox: tuple[Message, ...] = ()


@dataclass(frozen=True)
class Action:
    """An environment move plus an optional outgoing message."""

    move: Any
    message: str | None = None
    recipient: AgentId | None = None
    info: dict[str, Any] = field(default_factory=dict)


class Agent(Protocol):
    id: AgentId

    def act(self, observation: Observation) -> Action: ...

    def end_episode(self, episode: int) -> None: ...
