class Game:

    def __init__(self):
        self.score = 0

    def calculate_score(self):
        return self.score

    def roll(self, pins):
        self.score += pins
