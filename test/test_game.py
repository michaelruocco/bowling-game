import unittest
from src.game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_should_have_initial_score_zero(self):
        self.assertEqual(self.game.calculate_score(), 0)

    def test_gutter_game_should_score_zero(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.calculate_score(), 0)

    def test_game_of_all_ones_should_score_twenty(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.calculate_score(), 20)

    def roll_many(self, rolls, pins):
        for i in range(0, rolls):
            self.game.roll(pins)


if __name__ == '__main__':
    unittest.main()
