from sum_of_positive import positive_sum
from unittest import TestCase, main


class TestSumOfPositive (TestCase):
  
    def test_cases(self):

        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
    
    def test_empty_case(self):

        self.assertEqual(positive_sum([]),0)      

    def test_negative_case(self):

        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)

if __name__ == "__main__":
    main()