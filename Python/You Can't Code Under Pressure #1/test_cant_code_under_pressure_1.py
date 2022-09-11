from cant_code_under_pressure_1 import double_integer
from unittest import TestCase, main

class TestCantCodeUnderPressure1(TestCase):

    def test_case(self):

        self.assertEqual(double_integer(2), 4);
        self.assertEqual(double_integer(4), 8);
        self.assertEqual(double_integer(-10), -20);
        self.assertEqual(double_integer(0), 0);
        self.assertEqual(double_integer(100), 200);

if __name__ == "__main__":

    main()