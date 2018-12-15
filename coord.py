class Coord:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        :param other: Another Coord object
        :return: If self is equal to other and other is a Coord
        """
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __hash__(self):
        """
        For putting coords in sets or any situation a coord would need to be hashed
        :return: Hash of a Coord object
        """
        return hash((self.x, self.y))
