from are_you_playing_banjo import are_you_playing_banjo
from unittest import TestCase, main


class TestAreYouPlayingBanjo(TestCase):


    def test_cases(self):
        self.assertEqual(are_you_playing_banjo("martin"), "martin does not play banjo");
        self.assertEqual(are_you_playing_banjo("Rikke"), "Rikke plays banjo");
        self.assertEqual(are_you_playing_banjo("bravo"), "bravo does not play banjo")
        self.assertEqual(are_you_playing_banjo("rolf"), "rolf plays banjo")

if __name__ == "__main__":
    main()