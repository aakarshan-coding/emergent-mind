"""Belief tracking: does an agent correctly predict what another agent believes?"""

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(frozen=True)
class BeliefScore:
    correct: int
    total: int
    false_belief_correct: int
    false_belief_total: int

    @property
    def accuracy(self) -> float:
        return self.correct / self.total if self.total else 0.0

    @property
    def false_belief_accuracy(self) -> float:
        """Accuracy on items where the partner's belief differs from the truth.

        These are the informative cases: guessing that the partner believes the
        truth scores well elsewhere without modelling the partner at all.
        """
        if not self.false_belief_total:
            return 0.0
        return self.false_belief_correct / self.false_belief_total


def score_beliefs(
    predicted: Mapping[str, str],
    actual_beliefs: Mapping[str, str],
    world: Mapping[str, str],
) -> BeliefScore:
    """Compare predicted partner beliefs with their actual beliefs, per key."""
    correct = total = fb_correct = fb_total = 0
    for key, belief in actual_beliefs.items():
        hit = predicted.get(key) == belief
        total += 1
        correct += hit
        if world.get(key) != belief:
            fb_total += 1
            fb_correct += hit
    return BeliefScore(correct, total, fb_correct, fb_total)
