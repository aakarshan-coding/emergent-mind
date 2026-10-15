from emergent_mind.memory import MemoryEntry, MemoryStore
from emergent_mind.memory.interventions import delete_where, rewrite_where
from emergent_mind.types import AgentId

A = AgentId("a")


def store() -> MemoryStore:
    return MemoryStore(MemoryEntry(A, ep, 0, f"ep{ep}") for ep in range(3))


def test_delete_removes_matching_entries():
    s = store()
    assert delete_where(s, lambda e: e.episode == 1) == 1
    assert [e.content for e in s.entries()] == ["ep0", "ep2"]


def test_rewrite_changes_only_matching_entries():
    s = store()
    assert rewrite_where(s, lambda e: e.episode == 0, "false memory") == 1
    assert [e.content for e in s.entries()] == ["false memory", "ep1", "ep2"]
