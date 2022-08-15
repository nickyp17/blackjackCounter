class runningCount:
    def __init__(self):
        self._total = 0

    @property
    def total(self):
        return self._total

    def addLowCard(self):
        """Adds 1 to the count for any card with face value from 2-6"""
        self._total += 1
