"""Deterministic seeding so runs can be reproduced."""

import hashlib
import random


def derive_seed(base: int, *keys: object) -> int:
    """Derive a stable child seed from a base seed and any number of keys."""
    text = ":".join([str(base), *map(str, keys)])
    return int.from_bytes(hashlib.sha256(text.encode()).digest()[:8], "big")


def rng(base: int, *keys: object) -> random.Random:
    return random.Random(derive_seed(base, *keys))
