class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'({str(self.x)}, {str(self.y)})'

    def copy(self):
        return Point(self.x, self.y)

    def __hash__(self):
        return hash(f'{self.x}{self.y}')