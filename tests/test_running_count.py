from src.card_counter import RunningCount


def test_initializes_count_at_zero():
    """should initialize the running count total to 0"""
    count = RunningCount()

    assert count.total == 0


def test_add_low_card():
    """should add 1 to the total when a low card is pulled"""
    count = RunningCount()

    count.add_low_card()

    assert count.total == 1


def test_adds_two_low_cards():
    """should add to low cards to make a total of 2"""
    count = RunningCount()

    count.add_low_card()
    count.add_low_card()

    assert count.total == 2


def test_adds_high_card():
    """should add -1 to the count when a high card is drawn"""
    count = RunningCount()

    count.add_high_card()

    assert count.total == -1


def test_adds_high_and_low_card():
    """should add both a high and low card to make the total 0"""
    count = RunningCount()

    count.add_high_card()
    count.add_low_card()

    assert count.total == 0
