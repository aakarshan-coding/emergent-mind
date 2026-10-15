from emergent_mind.memory import MemoryEntry, MemoryStore
from emergent_mind.types import AgentId

A = AgentId("a")


def entry(step: int) -> MemoryEntry:
    return MemoryEntry(author=A, episode=0, step=step, content=f"s{step}")


def test_recent_returns_last_n_in_order():
    store = MemoryStore(entry(i) for i in range(5))
    assert [e.step for e in store.recent(2)] == [3, 4]
    assert store.recent(0) == []


def test_entries_returns_a_copy():
    store = MemoryStore([entry(0)])
    store.entries().clear()
    assert len(store) == 1
