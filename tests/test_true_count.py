from src.card_counter import RunningCount, TrueCount
from pytest import approx


def test_gets_true_count_with_running_count_of_zero():
    true_count = TrueCount(0, 6)

    assert true_count.total == 0


def test_gets_true_count_with_running_count_not_zero():
    true_count = TrueCount(8, 6)

    assert approx(true_count.total, 0.1) == 1.3
