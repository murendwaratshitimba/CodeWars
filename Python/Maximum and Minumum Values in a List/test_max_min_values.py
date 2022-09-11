from max_min_values import*
from unittest import TestCase, main



class TestMaxMinValues(TestCase):

    def test_min_cases(self):
        self.assertEqual(minimum([-52, 56, 30, 29, -54, 0, -110]), -110)
        self.assertEqual(minimum([42, 54, 65, 87, 0]), 0)
        self.assertEqual(minimum([1, 2, 3, 4, 5, 10]), 1)
        self.assertEqual(minimum([-1, -2, -3, -4, -5, -10]), -10)
        self.assertEqual(minimum([9]), 9)

   
    def test_max_cases(self):

        self.assertEqual(maximum([-52, 56, 30, 29, -54, 0, -110]), 56)
        self.assertEqual(maximum([4,6,2,1,9,63,-134,566]), 566)
        self.assertEqual(maximum([5]), 5)
        self.assertEqual(maximum([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
        self.assertEqual(maximum([9]), 9)

if __name__ == "__main__":
    main()