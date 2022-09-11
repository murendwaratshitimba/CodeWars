from multiply import multiply
from unittest import TestCase, main

class TestMultiply(TestCase):

   
    def test_cases(self):
        self.assertEqual(multiply(2,1), 2)

if __name__ == "__main__":

    main()

