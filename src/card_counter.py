class TrueCount:
    def __init__(self, running_count_total, number_of_decks):
        self._running_count_total = running_count_total
        self._number_of_decks = number_of_decks

    @property
    def total(self):
        return self._running_count_total / self._number_of_decks

    @property
    def number_of_decks(self):
        return self._number_of_decks

    def card_pulled(self, card_count):
        number_of_cards = self._number_of_decks * 52 - 1
        self._number_of_decks = number_of_cards / 52

        self._running_count_total += card_count


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
