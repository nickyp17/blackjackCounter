from src.card_counter import RunningCount, TrueCount
from pytest import approx


def test_gets_true_count_with_running_count_of_zero():
    true_count = TrueCount(0, 6)

    assert true_count.total == 0


def test_gets_true_count_with_running_count_not_zero():
    true_count = TrueCount(8, 6)

    assert approx(true_count.total, 0.1) == 1.3


def test_adjusts_deck_number_when_card_pulled():
    true_count = TrueCount(0, 6)

    true_count.card_pulled()

    assert approx(true_count.number_of_decks, 0.001) == 5.98


def test_adjusts_deck_number_when_two_cards_pulled():
    true_count = TrueCount(0, 6)

    true_count.card_pulled()
    true_count.card_pulled()

    assert approx(true_count.number_of_decks, 0.001) == 5.96
