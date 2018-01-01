import unittest
from src.game import Game


class GameTest(unittest.TestCase):

    def test_should_create_game(self):
        game = Game()

    def test_game_should_have_initial_score_zero(self):
        game = Game()
        self.assertEqual(game.calculate_score(), 0)


if __name__ == '__main__':
    unittest.main()
