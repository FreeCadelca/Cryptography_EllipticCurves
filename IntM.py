from Point import *


class IntM:
    def __init__(self, v: int, m: int):
        self.modulus = m
        self.value = v

    def __int__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError
            return IntM((self.value + other.value) % self.modulus, self.modulus)
        elif isinstance(other, int):
            return IntM((self.value + other) % self.modulus, self.modulus)
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError
            return IntM((self.value - other.value) % self.modulus, self.modulus)
        elif isinstance(other, int):
            return IntM((self.value - other) % self.modulus, self.modulus)
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError
            return IntM((self.value * other.value) % self.modulus, self.modulus)
        elif isinstance(other, int):
            return IntM((self.value * other) % self.modulus, self.modulus)
        else:
            raise ValueError

    def __floordiv__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError
            v = self.value
            while v % other.value != 0:
                v += self.modulus
            return IntM(v // other.value, self.modulus)
        elif isinstance(other, int):
            v = self.value
            while v % other != 0:
                v += self.modulus
            return IntM(v // other, self.modulus)
        else:
            raise ValueError

    def __pow__(self, power: int, modulo=None):
        v = 1
        for i in range(power):
            v *= self.value
            v %= self.modulus
        return IntM(v, self.modulus)

    def __gt__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError("The modules must match.")
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        else:
            raise ValueError

    def __lt__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError("The modules must match.")
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            raise ValueError

    def __ge__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError("The modules must match.")
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        else:
            raise ValueError

    def __le__(self, other):
        if isinstance(other, IntM):
            if self.modulus != other.modulus:
                raise ValueError("The modules must match.")
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        else:
            raise ValueError

    def __eq__(self, other):
        if isinstance(other, IntM):
            return self.modulus == other.modulus and self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            raise ValueError

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'{self.value}m{self.modulus}'


def make_intm_point(x: int, y: int, p: int):
    return Point(IntM(x, p), IntM(y, p))
