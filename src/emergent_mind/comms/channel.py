import random
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass

from emergent_mind.comms.disruption import Disruption
from emergent_mind.types import AgentId, Message


@dataclass(frozen=True)
class ChannelConfig:
    max_chars: int = 280
    max_messages_per_step: int = 1


class Channel:
    """Buffers messages for one step and delivers them under a communication budget."""

    def __init__(
        self,
        config: ChannelConfig | None = None,
        disruptions: Iterable[Disruption] = (),
        rng: random.Random | None = None,
    ) -> None:
        self.config = config or ChannelConfig()
        self.disruptions = list(disruptions)
        self.rng = rng or random.Random()
        self._pending: list[Message] = []
        self._sent_this_step: dict[AgentId, int] = defaultdict(int)

    def send(self, message: Message) -> bool:
        """Queue a message. Returns False if the sender is over budget for this step."""
        if self._sent_this_step[message.sender] >= self.config.max_messages_per_step:
            return False
        self._sent_this_step[message.sender] += 1
        content = message.content[: self.config.max_chars]
        self._pending.append(Message(message.sender, message.recipient, content, message.step))
        return True

    def deliver(self, agents: Iterable[AgentId]) -> dict[AgentId, list[Message]]:
        """Return each agent's inbox and reset the channel for the next step."""
        delivered = [m for m in map(self._disrupt, self._pending) if m is not None]
        inboxes = {a: [m for m in delivered if m.is_for(a)] for a in agents}
        self._pending.clear()
        self._sent_this_step.clear()
        return inboxes

    def _disrupt(self, message: Message) -> Message | None:
        for disruption in self.disruptions:
            result = disruption(message, self.rng)
            if result is None:
                return None
            message = result
        return message
