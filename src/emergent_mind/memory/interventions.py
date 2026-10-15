"""Memory interventions: delete or rewrite entries to test their causal role."""

from collections.abc import Callable
from dataclasses import replace

from emergent_mind.memory.store import MemoryEntry, MemoryStore

Predicate = Callable[[MemoryEntry], bool]


def delete_where(store: MemoryStore, predicate: Predicate) -> int:
    """Remove matching entries. Returns how many were removed."""
    kept = [e for e in store.entries() if not predicate(e)]
    removed = len(store) - len(kept)
    store.overwrite(kept)
    return removed


def rewrite_where(store: MemoryStore, predicate: Predicate, content: str) -> int:
    """Replace the content of matching entries. Returns how many were changed."""
    changed = 0
    entries = []
    for e in store.entries():
        if predicate(e):
            e = replace(e, content=content)
            changed += 1
        entries.append(e)
    store.overwrite(entries)
    return changed
