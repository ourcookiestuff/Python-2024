# Kod testujący moduł.
from fracs import *
import unittest


class TestFrac(unittest.TestCase):

    def test_init(self):
        frac = Frac(2, 4)
        self.assertEqual(frac.x, 1)
        self.assertEqual(frac.y, 2)

        with self.assertRaises(ValueError):
            Frac(1, 0)

    def test_str(self):
        self.assertEqual(str(Frac(3, 4)), "3/4")
        self.assertEqual(str(Frac(5, 1)), "5")

    def test_repr(self):
        self.assertEqual(repr(Frac(3, 4)), "Frac(3, 4)")

    def test_comparisons(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(6, 8)
        frac3 = Frac(1, 2)

        self.assertTrue(frac1 == frac2)
        self.assertTrue(frac1 != frac3)
        self.assertTrue(frac1 > frac3)
        self.assertTrue(frac1 == frac2)

    def test_addition(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(1, 4)

        self.assertEqual(frac1 + frac2, Frac(1, 1))
        self.assertEqual(frac1 + 1, Frac(7, 4))
        self.assertEqual(1 + frac2, Frac(5, 4))
        self.assertEqual(frac1 + 0.5, Frac(5, 4))

    def test_subtraction(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(1, 4)

        self.assertEqual(frac1 - frac2, Frac(1, 2))
        self.assertEqual(frac1 - 1, Frac(-1, 4))
        self.assertEqual(1 - frac2, Frac(3, 4))

    def test_multiplication(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(1, 2)

        self.assertEqual(frac1 * frac2, Frac(3, 8))
        self.assertEqual(frac1 * 2, Frac(6, 4))
        self.assertEqual(2 * frac1, Frac(6, 4))

    def test_division(self):
        frac1 = Frac(3, 4)
        frac2 = Frac(1, 2)

        self.assertEqual(frac1 / frac2, Frac(3, 2))
        self.assertEqual(frac1 / 2, Frac(3, 8))
        self.assertEqual(2 / frac1, Frac(8, 3))

    def test_float_conversion(self):
        frac = Frac(3, 4)
        self.assertEqual(float(frac), 0.75)


if __name__ == "__main__":
    unittest.main()
