

class runningCount:
    def __init__(self):
        self._total = 0

    @property
    def total(self):
        return self._total

    
    def addLowCard(self):
        self._total += 1