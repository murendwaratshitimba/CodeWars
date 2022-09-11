from reversed_string import solution
from unittest import TestCase, main

class TestReversedString(TestCase):

    def test_cases(self):

        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')

if __name__ == "__main__":
    main()