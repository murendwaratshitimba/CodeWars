from upper import make_upper_case
from unittest import TestCase, main

class TestUpper(TestCase):

    def test_cases(self):

        self.assertEqual(make_upper_case("hello"), "HELLO")

if __name__ == "__main__":
    main()