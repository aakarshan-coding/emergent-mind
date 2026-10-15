"""Uncertainty calibration: do stated confidences match accuracy?"""

from collections.abc import Sequence


def _check(confidences: Sequence[float], correct: Sequence[bool]) -> None:
    if len(confidences) != len(correct):
        raise ValueError("confidences and correct must have the same length")
    if not confidences:
        raise ValueError("need at least one prediction")
    if any(not 0.0 <= c <= 1.0 for c in confidences):
        raise ValueError("confidences must be in [0, 1]")


def brier_score(confidences: Sequence[float], correct: Sequence[bool]) -> float:
    """Mean squared error between confidence and outcome. Lower is better."""
    _check(confidences, correct)
    return sum((c - y) ** 2 for c, y in zip(confidences, correct, strict=True)) / len(correct)


def expected_calibration_error(
    confidences: Sequence[float], correct: Sequence[bool], bins: int = 10
) -> float:
    """Weighted mean gap between confidence and accuracy across equal-width bins."""
    _check(confidences, correct)
    buckets: list[list[tuple[float, bool]]] = [[] for _ in range(bins)]
    for c, y in zip(confidences, correct, strict=True):
        buckets[min(int(c * bins), bins - 1)].append((c, y))
    ece = 0.0
    for bucket in buckets:
        if bucket:
            mean_conf = sum(c for c, _ in bucket) / len(bucket)
            accuracy = sum(y for _, y in bucket) / len(bucket)
            ece += len(bucket) / len(correct) * abs(mean_conf - accuracy)
    return ece
