import unittest

import basic;

class basicTest(unittest.TestCase):
    def test_is_even(self):
        res = basic.is_even(4)
        self.assertEqual(res , True)
        res = basic.is_even(3)
        self.assertEqual(res ,False)

    def test_is_odd(self):
        res = basic.is_odd(3)
        self.assertEqual(res , True)
        res = basic.is_odd(4)
        self.assertEqual(res ,False)

    def test_square(self):
        res = basic.square(3)
        self.assertEqual(res , 9)
        res = basic.square(4)
        self.assertEqual(res ,16)
    def test_cube(self):
        res = basic.cube(3)
        self.assertEqual(res , 27)
        res = basic.cube(4)
        self.assertEqual(res ,64)

    def test_simple_interest(self):
        res = basic.simple_interest(200 ,3 ,4)
        self.assertEqual(res ,24)

    def test_sum_of_1_to_N(self):
        res = basic.sum_of_1_to_N(10)
        self.assertEqual(res ,55)

    def test_greatest_between_three(self):
        res = basic.greatest_between_three(1 ,5 ,3)
        self.assertEqual(res ,5)

    def test_average_of_three(self):
        res = basic.average_of_three(1 ,5 ,3)
        self.assertEqual(res ,3)
        res = basic.average_of_three(2,3,3)
        self.assertEqual(res ,2.67)


if __name__ == '__main__':
    unittest.main()
