from dataclasses import dataclass, field
from typing import Any, Protocol

from emergent_mind.types import AgentId


@dataclass(frozen=True)
class StepResult:
    """Per-agent outcome of one environment step, in the Gymnasium style."""

    views: dict[AgentId, dict[str, Any]]
    rewards: dict[AgentId, float]
    terminated: bool
    truncated: bool
    info: dict[str, Any] = field(default_factory=dict)


class MultiAgentEnv(Protocol):
    """A partially observable environment where all agents act simultaneously."""

    agents: list[AgentId]

    def reset(self, seed: int | None = None) -> dict[AgentId, dict[str, Any]]: ...

    def step(self, moves: dict[AgentId, Any]) -> StepResult: ...
