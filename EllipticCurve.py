from IntM import *


class EllipticCurve:
    def __init__(self, p, a, b):
        if -4 * a ** 3 - 27 * b ** 2 % p == 0:
            raise ValueError("p, a, b не проходят проверку на -4a^3 - 27b^2 ≠ 0 (mod p)")
        self.p = p
        self.a = a
        self.b = b
        self.points = []

    def sum_points(self, p1: Point, p2: Point):
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        if p1 == p2:
            new_x = ((p1.x * p1.x * 3 + self.a) / (p1.y * 2)) ** 2 - (p1.x * 2)
            new_y = ((p1.x * p1.x * 3 + self.a) / (p1.y * 2)) * (p1.x - new_x) - p1.y
            return Point(new_x, new_y)
        elif p1.x != p2.x:
            new_x = ((p2.y - p1.y) / (p2.x - p1.x)) ** 2 - p1.x - p2.x
            new_y = ((p2.y - p1.y) / (p2.x - p1.x)) * (p1.x - new_x) - p1.y
            return Point(new_x, new_y)
        else:
            return None
