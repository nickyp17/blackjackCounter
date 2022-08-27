class TrueCount:
    def __init__(self, running_count, number_of_decks):
        self._running_count = running_count
        self._number_of_decks = number_of_decks

    @property
    def total(self):
        return self._running_count.total / self._number_of_decks

    @property
    def number_of_decks(self):
        return self._number_of_decks

    def card_pulled(self):
        number_of_cards = self._number_of_decks * 52 - 1
        self._number_of_decks = number_of_cards / 52


class RunningCount:
    def __init__(self, total=0):
        self._total = total

    @property
    def total(self):
        return self._total

    def add_low_card(self):
        """Adds 1 to the count for any card with face value from 2-6"""
        self._total += 1

    def add_high_card(self):
        """Adds -1 to the count for any card with face value from 10-Ace"""
        self._total = -1
