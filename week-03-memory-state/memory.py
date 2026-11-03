"""
Day 1 - the sliding window: the session's working memory.

The window holds the last N exchanges, nothing older. What falls out
is gone; append() returns whatever fell out, so the loss is never
silent: the caller sees exactly which exchange left, and when.

>>>Defining the sliding window<<<
- max_exchanges defines how long the sliding window is, in numbers of exchanges.
- append() adds an exchange to the running exchanges list, and returns all of 
  the exchanges that have been forced out of the window.
  - get() returns the exchanges that are currently in the context window.
"""
# An exchange is one user turn plus the agent's full response (the model's
# reply and the Observation it produced). Count exchanges, never messages.
class SlidingWindow:
    """
    Holds the last user-defined number of exchanges, defined in the max_exchanges variable.
    append() returns the old exchanges that have fallen off.
    """

    def __init__(self, max_exchanges=10):
        self.max_exchanges = max_exchanges
        self.exchanges = []

    def append(self, exchange):
        """
        Adds one exchange and returns the list of all the exchanges that have been
        pushed out of the window.
        """
        self.exchanges.append(exchange)
        expired = []
        while len(self.exchanges) > self.max_exchanges:
            expired.append(self.exchanges.pop(0))
        return expired

    def get(self):
        """
        Returns the exchanges the model can see right now.
        """
        return list(self.exchanges)