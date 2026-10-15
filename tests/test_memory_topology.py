from emergent_mind.memory import MemoryEntry
from emergent_mind.memory.topology import individual, shared
from emergent_mind.types import AgentId

A, B = AgentId("a"), AgentId("b")


def test_individual_memories_are_isolated():
    mem = individual([A, B])
    mem[A].add(MemoryEntry(A, 0, 0, "secret"))
    assert len(mem[B]) == 0


def test_shared_memory_is_visible_to_all():
    mem = shared([A, B])
    mem[A].add(MemoryEntry(A, 0, 0, "note"))
    assert mem[B].entries()[0].content == "note"
