"""Assign memory stores to agents: one each, or one shared by all."""

from collections.abc import Iterable

from emergent_mind.memory.store import MemoryStore
from emergent_mind.types import AgentId


def individual(agents: Iterable[AgentId]) -> dict[AgentId, MemoryStore]:
    return {a: MemoryStore() for a in agents}


def shared(agents: Iterable[AgentId]) -> dict[AgentId, MemoryStore]:
    store = MemoryStore()
    return dict.fromkeys(agents, store)
