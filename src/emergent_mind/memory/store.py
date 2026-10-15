from collections.abc import Iterable
from dataclasses import dataclass

from emergent_mind.types import AgentId


@dataclass(frozen=True)
class MemoryEntry:
    author: AgentId
    episode: int
    step: int
    content: str


class MemoryStore:
    """An append-only log of memory entries, editable only through interventions."""

    def __init__(self, entries: Iterable[MemoryEntry] = ()) -> None:
        self._entries = list(entries)

    def add(self, entry: MemoryEntry) -> None:
        self._entries.append(entry)

    def overwrite(self, entries: Iterable[MemoryEntry]) -> None:
        """Replace all entries. Reserved for experimental interventions."""
        self._entries = list(entries)

    def entries(self) -> list[MemoryEntry]:
        return list(self._entries)

    def recent(self, n: int) -> list[MemoryEntry]:
        return self._entries[-n:] if n > 0 else []

    def __len__(self) -> int:
        return len(self._entries)
