import math


class Point():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ", " + str(self.direction) + ")"

    def move(self, speed):
        self.x = self.x + speed * math.cos((self.get_direction() + 90) * math.pi / 180)
        self.y = self.y + speed * math.sin((self.get_direction() - 90) * math.pi / 180)
        return round(self.x), round(self.y)

    def get_direction(self):
        return self.direction % 360
