import unittest
from fracs import add_frac, sub_frac, mul_frac, div_frac, is_positive, is_zero, cmp_frac, frac2float

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.positive_frac = [3, 4]
        self.negative_frac = [-3, 4]
        self.one = [1, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])

        self.assertEqual(add_frac([1, 2], self.zero), [1, 2])
        self.assertEqual(add_frac([3, 4], [-1, 4]), [1, 2])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 3], [1, 2]), [-1, 6])
        self.assertEqual(sub_frac([1, 3], [1, 3]), [0, 1])

        self.assertEqual(sub_frac([1, 2], self.zero), [1, 2])
        self.assertEqual(sub_frac([3, 4], [-1, 4]), [1, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([1, 2], [0, 1]), [0, 1])

        self.assertEqual(mul_frac([5, 3], self.one), [5, 3])
        self.assertEqual(mul_frac([-2, 3], [-3, 4]), [1, 2])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [3, 4]), [2, 3])
        self.assertEqual(div_frac([5, 3], self.one), [5, 3])
        self.assertEqual(div_frac([-2, 3], [-3, 4]), [8, 9])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive(self.zero))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([3, 4]), 0.75)
        self.assertAlmostEqual(frac2float([-1, 2]), -0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
