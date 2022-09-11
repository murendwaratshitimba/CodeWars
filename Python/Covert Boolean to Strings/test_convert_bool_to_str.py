from convert_bool_to_str import bool_to_word
from unittest import TestCase, main


class TestConvertBoolToStr(TestCase):
    
    def test_cases(self):

        self.assertEqual(bool_to_word(True), 'Yes')
        self.assertEqual(bool_to_word(False), 'No')

if __name__ == "__main__":
    main()