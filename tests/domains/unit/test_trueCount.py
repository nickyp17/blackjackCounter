from src.domains.trueCount import trueCount


def test_gets_true_count_with_zero_running_count():
    """should get the true count when the running count is 0 and with any number of decks"""
    count = trueCount(0, 8)

    assert count.total == 0


def test_gets_true_count_with_positive_running_count():
    """should get an acurate true count with a positive running count"""
    count = trueCount(8, 8)

    assert count.total == 1