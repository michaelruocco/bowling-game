class Game:

    def __init__(self):
        self.rolls = [0] * 21
        self.currentRoll = 0

    def calculate_score(self):
        score = 0
        firstInFrame = 0
        for frame in range(0, 10):
            if (self.__is_strike(firstInFrame)):
                score += self.__calculate_strike(firstInFrame)
                firstInFrame += 1
            elif (self.__is_spare(firstInFrame)):
                score += self.__calculate_spare(firstInFrame)
                firstInFrame += 2
            else:
                score += self.__calculate_frame(firstInFrame)
                firstInFrame += 2
        return score

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def __is_strike(self, firstInFrame):
        return self.rolls[firstInFrame] == 10

    def __is_spare(self, firstInFrame):
        return self.rolls[firstInFrame] + self.rolls[firstInFrame+1] == 10

    def __calculate_strike(self, firstInFrame):
        return 10 + self.rolls[firstInFrame+1] + self.rolls[firstInFrame+2]

    def __calculate_spare(self, firstInFrame):
        return 10 + self.rolls[firstInFrame+2]

    def __calculate_frame(self, firstInFrame):
        return self.rolls[firstInFrame] + self.rolls[firstInFrame+1]
