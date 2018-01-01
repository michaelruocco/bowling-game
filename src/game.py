class Game:

    def __init__(self):
        self.rolls = [0] * 23
        self.currentRoll = 0

    def calculate_score(self):
        return sum(self.rolls)

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1
