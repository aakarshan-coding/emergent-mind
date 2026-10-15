from emergent_mind.evaluation.beliefs import score_beliefs

WORLD = {"key": "box", "door": "locked"}
PARTNER = {"key": "basket", "door": "locked"}  # partner holds a false belief about the key


def test_reality_guesser_fails_false_belief_items():
    score = score_beliefs(predicted=WORLD, actual_beliefs=PARTNER, world=WORLD)
    assert score.accuracy == 0.5
    assert score.false_belief_accuracy == 0.0


def test_partner_model_passes_false_belief_items():
    score = score_beliefs(predicted=PARTNER, actual_beliefs=PARTNER, world=WORLD)
    assert score.accuracy == 1.0
    assert score.false_belief_accuracy == 1.0
