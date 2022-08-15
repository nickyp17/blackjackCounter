class trueCount:

    def __init__(self, runningCount, numberOfDecks):
        self._runningCount = runningCount
        self._numberOfDecks = numberOfDecks
        
    @property
    def total(self):
        return self._runningCount / self._numberOfDecks
