from vowel_count import get_count
from unittest import TestCase, main


class TestVoweCount(TestCase):
    

    """Should count all vowels"""
    def test_all_vowels(self):
        self.assertEqual(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")

    """Should not count \"y\""""
    def test_only_y(self):
        self.assertEqual(get_count("y"), 0, f"Incorrect answer for \"y\"")        

    """Should return 0 when no vowels"""
    def test_no_vowels_1(self):
        self.assertEqual(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")

    """Should return 0 for empty string"""
    def test_no_vowels_2(self):
        self.assertEqual(get_count(""), 0, f"Incorrect answer for empty string")

    """Should return 5 for \"abracadabra\""""
    def test_abracadabra(self):    
        self.assertEqual(get_count("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")

if __name__ == "__main__":
    main()