import unittest
from points import Point
from rectangles import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.A = Rectangle(0, 0, 4, 5)
        self.B = Rectangle(1, 1, 4, 5)
        self.C = Rectangle(4, 5, 0, 0)

    def test_str(self):
        self.assertEquals(str(self.A), "[(0, 0), (4, 5)]")
        self.assertEquals(str(self.B), "[(1, 1), (4, 5)]")

    def test_repr(self):
        self.assertEquals(repr(self.A), "Rectangle(0, 0, 4, 5)")
        self.assertEquals(repr(self.B), "Rectangle(1, 1, 4, 5)")

    def test_qe(self):
        self.assertTrue(self.A == self.A)
        self.assertTrue(self.A == self.C)
        self.assertFalse(self.A == self.B)

    def test_ne(self):
        self.assertTrue(self.A != self.B)
        self.assertFalse(self.A != self.A)

    def test_center(self):
        self.assertEquals(self.A.center(), Point(2, 2.5))
        self.assertEquals(self.B.center(), Point(2.5, 3))

    def test_area(self):
        self.assertEquals(self.A.area(), 20)
        self.assertEquals(self.B.area(), 12)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
