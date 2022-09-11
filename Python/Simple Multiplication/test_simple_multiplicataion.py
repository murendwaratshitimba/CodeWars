from simple_multiplication import simple_multiplication
from unittest import TestCase, main


class TestSimpleMultiplication(TestCase):

    def test_cases(self):

        self.assertEqual(simple_multiplication(2), 16)
        self.assertEqual(simple_multiplication(1), 9)
        self.assertEqual(simple_multiplication(8), 64)
        self.assertEqual(simple_multiplication(4), 32)
        self.assertEqual(simple_multiplication(5), 45)

if __name__ == "__main__":
    main()