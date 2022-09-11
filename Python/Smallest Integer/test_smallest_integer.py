from smallest_integer import find_smallest_int
from unittest import TestCase, main


class TestSmallestInteger(TestCase):

    def test_cases(self):
        self.assertEqual(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        self.assertEqual(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        self.assertEqual(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)

if __name__ == "__main__":
    main()