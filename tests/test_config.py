import pytest

from emergent_mind.experiments import Condition, ExperimentConfig


@pytest.mark.parametrize(
    ("condition", "communicates", "shares", "self_model"),
    [
        (Condition.INDEPENDENT, False, False, False),
        (Condition.COMMUNICATING, True, False, False),
        (Condition.SHARED_MEMORY, True, True, False),
        (Condition.SELF_MODEL, True, False, True),
    ],
)
def test_condition_flags_match_research_plan(condition, communicates, shares, self_model):
    assert condition.communicates is communicates
    assert condition.shares_memory is shares
    assert condition.has_self_model is self_model


def test_rejects_single_agent():
    with pytest.raises(ValueError):
        ExperimentConfig(Condition.COMMUNICATING, num_agents=1)
