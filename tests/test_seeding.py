from emergent_mind.seeding import derive_seed, rng


def test_same_keys_give_same_seed():
    assert derive_seed(42, "episode", 3) == derive_seed(42, "episode", 3)


def test_different_keys_give_different_seeds():
    assert derive_seed(42, "episode", 3) != derive_seed(42, "episode", 4)


def test_rng_streams_are_reproducible():
    assert rng(1, "x").random() == rng(1, "x").random()
