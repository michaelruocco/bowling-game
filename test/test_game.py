import unittest
from src.game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_should_have_initial_score_zero(self):
        self.assertEqual(self.game.calculate_score(), 0)

    def test_gutter_game_should_score_zero(self):
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.calculate_score(), 0)

    def test_game_of_all_ones_should_score_twenty(self):
        for i in range(0, 20):
            self.game.roll(1)
        self.assertEqual(self.game.calculate_score(), 20)


if __name__ == '__main__':
    unittest.main()
