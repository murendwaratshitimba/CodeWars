from abbreviate import abbrev_name
from unittest import TestCase, main


class TestAbbreviate(TestCase):

    def test_cases(self):

        self.assertEqual(abbrev_name("Sam Harris"), "S.H")
        self.assertEqual(abbrev_name("patrick feenan"), "P.F")
        self.assertEqual(abbrev_name("Evan C"), "E.C")
        self.assertEqual(abbrev_name("P Favuzzi"), "P.F")
        self.assertEqual(abbrev_name("David Mendieta"), "D.M")

if __name__ == "__main__":
    main()