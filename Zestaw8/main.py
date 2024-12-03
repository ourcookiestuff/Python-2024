import unittest
from points import Point
from rectangles import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(0, 0, 4, 4)
        self.assertEqual(rect.pt1, Point(0, 0))
        self.assertEqual(rect.pt2, Point(4, 4))
        with self.assertRaises(ValueError):
            Rectangle(4, 4, 0, 0)

    def test_str_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_equality(self):
        rect1 = Rectangle(1, 1, 4, 4)
        rect2 = Rectangle(1, 1, 4, 4)
        rect3 = Rectangle(0, 0, 3, 3)
        self.assertEqual(rect1, rect2)
        self.assertNotEqual(rect1, rect3)

    def test_area(self):
        rect = Rectangle(0, 0, 4, 4)
        self.assertEqual(rect.area(), 16)

    def test_move(self):
        rect = Rectangle(0, 0, 2, 2)
        moved = rect.move(1, 1)
        self.assertEqual(moved, Rectangle(1, 1, 3, 3))

    def test_intersection(self):
        rect1 = Rectangle(0, 0, 4, 4)
        rect2 = Rectangle(2, 2, 6, 6)
        inter = rect1.intersection(rect2)
        self.assertEqual(inter, Rectangle(2, 2, 4, 4))
        with self.assertRaises(ValueError):
            rect1.intersection(Rectangle(5, 5, 7, 7))

    def test_cover(self):
        rect1 = Rectangle(0, 0, 4, 4)
        rect2 = Rectangle(2, 2, 6, 6)
        cover = rect1.cover(rect2)
        self.assertEqual(cover, Rectangle(0, 0, 6, 6))

    def test_make4(self):
        rect = Rectangle(0, 0, 4, 4)
        sub_rects = rect.make4()
        self.assertEqual(sub_rects[0], Rectangle(0, 0, 2, 2))
        self.assertEqual(sub_rects[1], Rectangle(2, 0, 4, 2))
        self.assertEqual(sub_rects[2], Rectangle(0, 2, 2, 4))
        self.assertEqual(sub_rects[3], Rectangle(2, 2, 4, 4))

    def test_from_points(self):
        pt1 = Point(0, 0)
        pt2 = Point(4, 4)
        rect = Rectangle.from_points([pt1, pt2])
        self.assertEqual(rect, Rectangle(0, 0, 4, 4))
        with self.assertRaises(ValueError):
            Rectangle.from_points([pt1])

    def test_properties(self):
        rect = Rectangle(1, 1, 5, 5)
        self.assertEqual(rect.top, 5)
        self.assertEqual(rect.bottom, 1)
        self.assertEqual(rect.left, 1)
        self.assertEqual(rect.right, 5)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.topleft, Point(1, 5))
        self.assertEqual(rect.bottomleft, Point(1, 1))
        self.assertEqual(rect.topright, Point(5, 5))
        self.assertEqual(rect.bottomright, Point(5, 1))
        self.assertEqual(rect.center, Point(3, 3))


if __name__ == "__main__":
    unittest.main()
