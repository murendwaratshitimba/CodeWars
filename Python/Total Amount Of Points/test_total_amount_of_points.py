from total_amount_of_points import points
from unittest import TestCase, main


class TestTotalAmountOfPoints(TestCase):

    def test_cases(self):
        self.assertEqual(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']), 30)
        self.assertEqual(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']), 10)
        self.assertEqual(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']), 0)
        self.assertEqual(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']), 15)
        self.assertEqual(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']), 12)

if __name__ == "__main__":

    main()