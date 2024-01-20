import random

class Conqueror:
    def __init__(self):
        self.score = random.randint(1, 100)
        self.multiply = random.randint(1, 3)
        self.money_per_second = random.randint(1, 3)

    def update(self):
        self.score += self.money_per_second * self.multiply

    def add_multiply(self, added_value):
        self.multiply += added_value

    def get_score(self):
        return self.score
