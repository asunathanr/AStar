from coord import Coord


class WeightedCoord(Coord):
    def __init__(self, weight, x, y, parent=None):
        super().__init__(x, y)
        self.h = 0
        self.weight = weight
        self.f = 0
        self.parent = parent

    def set_f(self):
        self.f = self.weight + self.h

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return isinstance(other, self.__class__) and self.weight < other.weight

    def __str__(self):
        str_parent = '' if self.parent is None else str(self.parent.x) + ' ' + str(self.parent.y)
        return ' (' + str(self.x) + ' ' + str(self.y) + ')' + ' Parent: ' + str_parent

    def __hash__(self):
        return hash((self.x, self.y))
