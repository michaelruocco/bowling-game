import unittest
from src.game import Game


class GameTest(unittest.TestCase):

    def test_should_create_game(self):
        game = Game()


if __name__ == '__main__':
    unittest.main()
