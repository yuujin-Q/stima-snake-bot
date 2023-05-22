import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def to_string(self):
        return f"({self.x}, {self.y})"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    @staticmethod
    def manhattan_distance(p1, p2):
        difference = p1 - p2
        return abs(difference.get_x()) + abs(difference.get_y())

    @staticmethod
    def euclidean_distance(p1, p2):
        return math.sqrt((p1.get_x() - p2.get_x()) ** 2 + (p1.get_y() - p2.get_y()) ** 2)
