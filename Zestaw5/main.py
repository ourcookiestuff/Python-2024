import unittest
from polys import add_poly, sub_poly, mul_poly, is_zero, eq_poly, eval_poly, combine_poly, pow_poly, diff_poly

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2
        self.p3 = [3, 2, 1]  # W(x) = x^2 + 2x + 3
        self.zero_poly = [0]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p3, self.p1), [3, 3, 1])  # W(x) = x^2 + 3x + 3

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p3, self.p1), [3, 1, 1])  # W(x) = x^2 + x + 3
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])  # W(x) = x^2 - x

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])  # W(x) = x^3
        self.assertEqual(mul_poly(self.p3, self.p1), [0, 3, 2, 1])  # W(x) = x^3 + 2x^2 + 3x

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero_poly))  # Wielomian zero
        self.assertFalse(is_zero(self.p1))  # W(x) = x
        self.assertTrue(is_zero([0, 0, 0]))  # Wielomian zero z dodatkowymi zerami

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p1, [0, 1]))  # W(x) = x
        self.assertTrue(eq_poly([1, 0, 0], [1]))  # Redukcja zer na końcu
        self.assertFalse(eq_poly(self.p2, self.p3))  # W(x) = x^2 vs W(x) = x^2 + 2x + 3

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 2), 2)  # W(2) = 2 dla W(x) = x
        self.assertEqual(eval_poly(self.p2, 3), 9)  # W(3) = 9 dla W(x) = x^2
        self.assertEqual(eval_poly(self.p3, 1), 6)  # W(1) = 6 dla W(x) = x^2 + 2x + 3

    def test_combine_poly(self): pass

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 2), [0, 0, 1])  # W(x)^2 = x^2 dla W(x) = x
        self.assertEqual(pow_poly(self.p3, 3), [27, 54, 63, 44, 21, 6, 1])  # (x^2 + 2x + 3)^3

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])  # W'(x) = 1 dla W(x) = x
        self.assertEqual(diff_poly(self.p2), [0, 2])  # W'(x) = 2x dla W(x) = x^2
        self.assertEqual(diff_poly(self.p3), [2, 2])  # W'(x) = 2x + 2 dla W(x) = x^2 + 2x + 3

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()  # Uruchamia wszystkie testy