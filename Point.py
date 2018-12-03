import math


class Point():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, speed):
        self.x = round(self.x + speed * math.cos((self.get_direction() + 90) * math.pi / 180))
        self.y = round(self.y + speed * math.sin((self.get_direction() - 90) * math.pi / 180))
        return self.x, self.y

    def get_direction(self):
        return self.direction % 360
