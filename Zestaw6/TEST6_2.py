import unittest
from points import Point


class TestPoint(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Point(2, 3)), "(2, 3)")

    def test_repr(self):
        self.assertEqual(repr(Point(2, 3)), "Point(2, 3)")

    def test_eq(self):
        self.assertTrue(Point(2, 3) == Point(2, 3))
        self.assertFalse(Point(2, 3) == Point(4, 5))

    def test_ne(self):
        self.assertTrue(Point(2, 3) != Point(4, 5))
        self.assertFalse(Point(2, 3) != Point(2, 3))

    def test_add(self):
        self.assertEqual(Point(2, 3) + Point(4, 5), Point(6, 8))

    def test_sub(self):
        self.assertEqual(Point(4, 5) - Point(2, 3), Point(2, 2))

    def test_mul(self):
        self.assertEqual(Point(2, 3) * Point(4, 5), 23)

    def test_cross(self):
        self.assertEqual(Point(2, 3).cross(Point(4, 5)), -2)

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)

    def test_hash(self):
        self.assertEqual(hash(Point(2, 3)), hash((2, 3)))
        self.assertNotEqual(hash(Point(2, 3)), hash((3, 4)))


if __name__ == "__main__":
    unittest.main()
