class ClosedSet:
    """
    Closed set used in A* implementation.
    """
    def __init__(self):
        self.closed = set()

    def add(self, item, weight) -> None:
        self.closed.add(item)

    def find(self, item) -> bool:
        return item in self.closed