from string_to_array import string_to_array
from unittest import TestCase, main


class TestStringToArray(TestCase):

    def test_cases(self):
        
        self.assertEqual(string_to_array("Robin Singh"), ["Robin", "Singh"])
        self.assertEqual(string_to_array("CodeWars"), ["CodeWars"])
        self.assertEqual(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
        self.assertEqual(string_to_array("1 2 3"), ["1", "2", "3"])
        self.assertEqual(string_to_array(""), [""])

if __name__ == "__main__":
    main()