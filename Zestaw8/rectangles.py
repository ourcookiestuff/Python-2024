from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Nieprawidłowe współrzędne prostokąta: x1 < x2 i y1 < y2.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1 != other.pt1 and self.pt1 != other.pt2:
            return False
        if self.pt2 != other.pt1 and self.pt2 != other.pt2:
            return False
        return True

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def area(self):             # pole powierzchni
        a = abs(self.pt1.x - self.pt2.x)
        b = abs(self.pt1.y - self.pt2.y)

        return a * b

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(
            self.pt1.x + x, self.pt1.y + y,
            self.pt2.x + x, self.pt2.y + y
        )

    def intersection(self, other):   # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            raise ValueError("Prostokąty nie mają części wspólnej.")

    def cover(self, other):     # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):            # zwraca krotkę czterech mniejszych
        center = self.center
        return (
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),
        )
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Do utworzenia prostokąta wymagane są dwa punkty!!!")

        pt1, pt2 = points
        return cls(pt1.x, pt1.y, pt2.x, pt2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point(
            (self.pt1.x + self.pt2.x) / 2,
            (self.pt1.y + self.pt2.y) / 2
        )
