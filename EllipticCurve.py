from IntM import *
import math


isDebug = 0


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


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
        if p1.y == 0 and p2.y == 0:
            return None
        try:
            if p1 == p2:
                # t1 = p1.x * p1.x * 3 + self.a
                # t2 = p1.y * 2
                # t3 = t1 // t2
                # t4 = t3 ** 2
                # t5 = p1.x * 2
                # new_x = t4 - t5
                new_x = ((p1.x * p1.x * 3 + self.a) // (p1.y * 2)) ** 2 - (p1.x * 2)
                new_y = ((p1.x * p1.x * 3 + self.a) // (p1.y * 2)) * (p1.x - new_x) - p1.y
                return Point(new_x, new_y)
            elif p1.x != p2.x:
                new_x = ((p2.y - p1.y) // (p2.x - p1.x)) ** 2 - p1.x - p2.x
                new_y = ((p2.y - p1.y) // (p2.x - p1.x)) * (p1.x - new_x) - p1.y
                return Point(new_x, new_y)
            else:
                return None
        except ValueError:
            return None

    def inv_point(self, p: Point):
        return Point(p.x, p.y * (-1))

    def find_points(self):
        print(f'<Finding orders func>') if isDebug else ''
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
        print(f'<Finding orders func end>') if isDebug else ''
        return self.points

    def find_orders(self):
        print(f'<find_orders func>') if isDebug else ''
        orders = dict()
        if not len(self.points):
            self.find_points()
        for i in range(len(self.points)):
            print(f'i = {self.points[i]}:') if isDebug else ''
            if self.points[i] is None:
                orders[None] = 1
                print(f'\torder({self.points[i]}) = 1') if isDebug else ''
                continue

            cur_multyplying = self.points[i].copy()
            count = 1
            print(f'\tcount = {count}, cur:{cur_multyplying}') if isDebug else ''
            while cur_multyplying is not None:
                cur_multyplying = self.sum_points(cur_multyplying, self.points[i])
                count += 1
                print(f'\tcount = {count}, cur:{cur_multyplying}') if isDebug else ''
            orders[self.points[i]] = count
            print(f'\torder({self.points[i]}) = {count}') if isDebug else ''
        print(f'<find_orders func end>') if isDebug else ''
        return orders

    def calculate_multiplicity(self, p: Point, k: int):
        print(f'<calculate_multiplicity func>') if isDebug else ''
        cur_sum = None
        for count in range(1, k + 1):
            cur_sum = self.sum_points(cur_sum, p)
            print(f'\tcount = {count}, cur_sum:{cur_sum}') if isDebug else ''
        print(f'<calculate_multiplicity func end>') if isDebug else ''
        return cur_sum

    def find_prime_subgroups(self):
        print(f'<find_prime_subgroups func>') if isDebug else ''
        orders = self.find_orders()
        for p in orders.keys():
            if is_prime(orders[p]):
                print(f'O({p}) is prime') if isDebug else ''
                cur_subgroup = [p.copy()]
                cur_multyplying = p.copy()
                while cur_multyplying is not None:
                    cur_multyplying = self.sum_points(cur_multyplying, p)
                    cur_subgroup.append(cur_multyplying)
                print("subgroup with prime order: {" + f"{cur_subgroup[0]}; ", end='')
                for i in cur_subgroup:
                    print(i, "; ", sep='', end='')
                print('}')
        print(f'<find_prime_subgroups func end>') if isDebug else ''


curve = EllipticCurve(3, -4, 13)
print("Number of points: ", len(curve.find_points()))
print(*curve.find_points())
orders = curve.find_orders()
for i in orders.keys():
    print(f'Order({i}) = {orders[i]}')
curve.find_prime_subgroups()

print(f'3P(12; 3) = {curve.calculate_multiplicity(Point(IntM(7, 13), IntM(3, 13)), 3)}')
