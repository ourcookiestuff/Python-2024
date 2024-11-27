from math import gcd


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Mianownik nie może być zerem.")
        self.x = x
        self.y = y
        if self.y < 0:
            self.x *= -1
            self.y *= -1
        g = gcd(self.x, self.y)
        self.x //= g
        self.y //= g
        if self.y < 0:
            self.x = -self.x
            self.y = -self.y

    def __str__(self):          # zwraca "x/y" lub "x" dla y=1
        if self.y != 1:
            return f"{self.x}/{self.y}"
        else:
            return f"{self.x}"

    def __repr__(self):         # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    # Py2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other):
        if isinstance(other, Frac):
            return self.x * other.y == self.y * other.x
        elif isinstance(other, int):
            return self.x == other * self.y
        elif isinstance(other, float):
            return self == Frac(*float(other).as_integer_ratio())
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Frac):
            return self.x * other.y < self.y * other.x
        elif isinstance(other, int):
            return self.x < other * self.y
        elif isinstance(other, float):
            return self < Frac(*float(other).as_integer_ratio())
        return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):   # frac1+frac2, frac+int
        if isinstance(other, Frac):
            return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x + self.y * other, self.y)
        elif isinstance(other, float):
            return self + Frac(*float(other).as_integer_ratio())
        return NotImplemented

    __radd__ = __add__              # int+frac

    def __sub__(self, other):   # frac1-frac2, frac-int
        if isinstance(other, Frac):
            return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x - self.y * other, self.y)
        elif isinstance(other, float):
            return self - Frac(*float(other).as_integer_ratio())
        return NotImplemented

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):   # frac1*frac2, frac*int
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x * other, self.y)
        elif isinstance(other, float):
            return self * Frac(*float(other).as_integer_ratio())
        return NotImplemented

    __rmul__ = __mul__              # int*frac

    # def __div__(self, other): pass  # frac1/frac2, frac/int, Py2

    # def __rdiv__(self, other): pass  # int/frac, Py2

    def __truediv__(self, other):   # frac1/frac2, frac/int, Py3
        if isinstance(other, Frac):
            return Frac(self.x * other.y, self.y * other.x)
        elif isinstance(other, int):
            return Frac(self.x, self.y * other)
        elif isinstance(other, float):
            return self / Frac(*float(other).as_integer_ratio())
        return NotImplemented

    def __rtruediv__(self, other):   # int/frac, Py3
        if isinstance(other, int):
            return Frac(other * self.y, self.x)
        return NotImplemented

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):          # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])



