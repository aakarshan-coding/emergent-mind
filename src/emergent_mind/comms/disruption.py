"""Channel interventions: drop or corrupt messages in transit."""

import random
from collections.abc import Callable
from dataclasses import replace

from emergent_mind.types import Message

Disruption = Callable[[Message, random.Random], Message | None]


def drop(p: float) -> Disruption:
    """Drop each message with probability p."""

    def apply(message: Message, rng: random.Random) -> Message | None:
        return None if rng.random() < p else message

    return apply


def shuffle_words(p: float) -> Disruption:
    """With probability p, shuffle the words of a message."""

    def apply(message: Message, rng: random.Random) -> Message | None:
        if rng.random() >= p:
            return message
        words = message.content.split()
        rng.shuffle(words)
        return replace(message, content=" ".join(words))

    return apply
