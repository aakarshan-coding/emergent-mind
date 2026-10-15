from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass

from emergent_mind.types import AgentId, Message


@dataclass(frozen=True)
class ChannelConfig:
    max_chars: int = 280
    max_messages_per_step: int = 1


class Channel:
    """Buffers messages for one step and delivers them under a communication budget."""

    def __init__(self, config: ChannelConfig | None = None) -> None:
        self.config = config or ChannelConfig()
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
        inboxes = {a: [m for m in self._pending if m.is_for(a)] for a in agents}
        self._pending.clear()
        self._sent_this_step.clear()
        return inboxes
