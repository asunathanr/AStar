from coord import Coord


class WeightedCoord(Coord):
    def __init__(self, weight, x, y):
        super().__init__(x, y)
        self.h = 0
        self.weight = weight
        self.parent = None

    def f(self):
        return self.weight + self.h

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return isinstance(other, self.__class__) and self.f() < other.f()

    def __str__(self):
        str_parent = '' if self.parent is None else str(self.parent.x) + ' ' + str(self.parent.y)
        return 'Weight: ' + str(self.weight) + ' (' + str(self.x) + ' ' + str(self.y) + ')' + ' Parent: ' + str_parent

    def __hash__(self):
        return hash((self.weight, self.x, self.y))
