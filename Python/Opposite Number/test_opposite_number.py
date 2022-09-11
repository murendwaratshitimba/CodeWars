from opposite_number import opposite
from unittest import TestCase, main

class TestOppositeNumber(TestCase):

    def test_cases(self):

        self.assertEqual(opposite(1),-1)
        self.assertEqual(opposite(25.6), -25.6)
        self.assertEqual(opposite(0), 0)
        self.assertEqual(opposite(1425.2222), -1425.2222)
        self.assertEqual(opposite(-3.1458), 3.1458)
        self.assertEqual(opposite(-95858588225),95858588225)
    
if __name__ == "__main__":
    main()