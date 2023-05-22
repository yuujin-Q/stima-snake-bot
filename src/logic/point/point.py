class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    @staticmethod
    def manhattan_distance(p1, p2):
        difference = p1 - p2
        return abs(difference.get_x()) + abs(difference.get_y())
