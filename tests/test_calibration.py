import pytest

from emergent_mind.evaluation.calibration import brier_score, expected_calibration_error


def test_perfect_confident_predictions_score_zero():
    assert brier_score([1.0, 0.0], [True, False]) == 0.0
    assert expected_calibration_error([1.0, 0.0], [True, False]) == 0.0


def test_overconfidence_is_penalized():
    # Always 90% confident, right only half the time.
    conf, correct = [0.9] * 4, [True, False, True, False]
    assert expected_calibration_error(conf, correct) == pytest.approx(0.4)
    assert brier_score(conf, correct) == pytest.approx((0.01 + 0.81) / 2)


def test_well_calibrated_half_confidence():
    assert expected_calibration_error([0.5] * 4, [True, False, True, False]) == 0.0


def test_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        brier_score([0.5], [True, False])
