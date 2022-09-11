from math_operators import basic_op
from unittest import TestCase, main


class TestMathOperators(TestCase):


    def test_cases(self):
        self.assertEqual(basic_op('+', 4, 7), 11)
        self.assertEqual(basic_op('-', 15, 18), -3)
        self.assertEqual(basic_op('*', 5, 5), 25)
        self.assertEqual(basic_op('/', 49, 7), 7)

if __name__ == "__main__":
    main()