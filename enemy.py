import random
from base_plane import BasePlane


class Enemy(BasePlane):

    def __init__(self, ai_settings, screen):
        BasePlane.__init__(self, ai_settings, screen, "images/ship6small.png")

        self.min = random.randint(0, 30) - 30
        self.max = random.randint(0, 30)
        self.speed = random.randint(1, 3)
        self.counter = 0

    def update(self):
        self.counter = self.counter + 1
        if self.counter % 10 == 0:
            x = random.randint(self.min, self.max)
            self.turn(x)

        self.drive(self.speed)
