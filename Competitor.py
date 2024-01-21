import random
from Settings import *


class Competitor:
    def __init__(self):
        self.score = 0.0
        self.multiply = random.randint(1, 3)
        self.money_per_second = random.randint(1, 3)

    def update(self):
        self.score += self.money_per_second * self.multiply / FPS
        if self.score % 50 == 0:
            self.add_multiply(random.randint(1, 3))

    def add_multiply(self, added_value):
        self.multiply += added_value

    def get_score(self):
        return int(self.score)
