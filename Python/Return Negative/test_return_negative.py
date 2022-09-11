from return_negaive import make_negative
from unittest import TestCase, main

class TestReturnNegative(TestCase):

    def test_cases(self):

        for n, expected in ((42,-42), (-9,-9), (0,0)):

            actual = make_negative(n)
            message = f"For n = {n}, expected {expected} but got {actual}"
            self.assertEqual(actual, expected, message)

if __name__ == "__main__":

    main()