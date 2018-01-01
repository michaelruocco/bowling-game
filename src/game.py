class Game:

    def __init__(self):
        self.rolls = [0] * 23
        self.currentRoll = 0

    def calculate_score(self):
        score = 0
        firstInFrame = 0
        for frame in range(0, 10):
            if (self.rolls[firstInFrame] + self.rolls[firstInFrame+1] == 10):
                score += 10 + self.rolls[firstInFrame+2]
            else:
                score += self.rolls[firstInFrame] + self.rolls[firstInFrame+1]
            firstInFrame += 2
        return score

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1
