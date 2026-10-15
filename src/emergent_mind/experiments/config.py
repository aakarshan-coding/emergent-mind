from dataclasses import dataclass, field
from enum import StrEnum

from emergent_mind.comms import ChannelConfig


class Condition(StrEnum):
    INDEPENDENT = "independent"
    COMMUNICATING = "communicating"
    SHARED_MEMORY = "shared_memory"
    SELF_MODEL = "self_model"

    @property
    def communicates(self) -> bool:
        return self is not Condition.INDEPENDENT

    @property
    def shares_memory(self) -> bool:
        return self is Condition.SHARED_MEMORY

    @property
    def has_self_model(self) -> bool:
        return self is Condition.SELF_MODEL


@dataclass(frozen=True)
class ExperimentConfig:
    condition: Condition
    num_agents: int = 3
    episodes: int = 50
    max_steps: int = 30
    seed: int = 0
    channel: ChannelConfig = field(default_factory=ChannelConfig)

    def __post_init__(self) -> None:
        if self.num_agents < 2:
            raise ValueError("multi-agent experiments need at least 2 agents")
        if self.episodes < 1 or self.max_steps < 1:
            raise ValueError("episodes and max_steps must be positive")
