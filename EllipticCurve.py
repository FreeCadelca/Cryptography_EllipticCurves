from IntM import *

isDebug = 1


class EllipticCurve:
    def __init__(self, a, b, p):
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
        try:
            if p1 == p2:
                new_x = ((p1.x * p1.x * 3 + self.a) // (p1.y * 2)) ** 2 - (p1.x * 2)
                new_y = ((p1.x * p1.x * 3 + self.a) // (p1.y * 2)) * (p1.x - new_x) - p1.y
                return Point(new_x, new_y)
            elif p1.x != p2.x:
                new_x = ((p2.y - p1.y) // (p2.x - p1.x)) ** 2 - p1.x - p2.x
                new_y = ((p2.y - p1.y) // (p2.x - p1.x)) * (p1.x - new_x) - p1.y
                return Point(new_x, new_y)
            else:
                return None
        except ZeroDivisionError:
            return None

    def find_points(self):
        if len(self.points):
            return self.points
        F_p = [i for i in range(self.p)]
        sq_degrees = dict()
        for i in F_p:
            sq = (i * i) % self.p
            if not sq in sq_degrees.keys():
                sq_degrees[sq] = [i]
            else:
                sq_degrees[sq].append(i)
        # print(sq_degrees)

        self.points.append(None)
        for x in range(self.p):
            print(f'x = {x}:') if isDebug else ''
            xm = IntM(x, self.p)
            x3xb = xm ** 3 + xm * self.a + self.b
            print(f'\tx3xb = {x3xb}') if isDebug else ''
            if x3xb.value in sq_degrees.keys():
                print(f'\tsquare roots - {sq_degrees[x3xb.value]}:') if isDebug else ''
                for sq_root in sq_degrees[x3xb.value]:
                    self.points.append(Point(IntM(x, self.p), IntM(sq_root, self.p)))
                    print(f'\tadded point {Point(IntM(x, self.p), IntM(sq_root, self.p))}') if isDebug else ''
        return self.points


curve = EllipticCurve(1, 7, 17)
curve.find_points()
