from ast import main
from hello_world import greet
from unittest import TestCase, main


class TestHelloWorld(TestCase):

    def test_greet(self):

        self.assertEqual(greet(), "hello world!", "Greet doesn't return hello world!")

if __name__ == "__main__":

    main()