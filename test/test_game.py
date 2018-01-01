import unittest
from src.game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_score_zero(self):
        self.assertEqual(self.game.calculate_score(), 0)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.calculate_score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.calculate_score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.calculate_score(), 16)

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.calculate_score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.calculate_score(), 300)

    def roll_many(self, rolls, pins):
        for i in range(0, rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.roll_many(2, 5)

    def roll_strike(self):
        self.game.roll(10)


if __name__ == '__main__':
    unittest.main()
