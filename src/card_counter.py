class TrueCount:
    def __init__(self, running_count, number_of_decks):
        self._running_count = running_count
        self._number_of_decks = number_of_decks

    @property
    def total(self):
        return self._running_count / self._number_of_decks


class RunningCount:
    def __init__(self):
        self._total = 0

    @property
    def total(self):
        return self._total

    def add_low_card(self):
        """Adds 1 to the count for any card with face value from 2-6"""
        self._total += 1

    def add_high_card(self):
        """Adds -1 to the count for any card with face value from 10-Ace"""
        self._total = -1
