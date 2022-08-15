class TrueCount:
    def __init__(self):
        pass


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
