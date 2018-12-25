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

    def turn(self, delta):
        self.direction += delta

    def is_in_area(self, ai_settings):
        return self.x >= 0 \
            and self.x <= ai_settings.screen_width \
            and self.y >= 0 \
            and self.y <= ai_settings.screen_height

    def to_point(self):
        return (int(self.x), int(self.y))

    def distance_to(self, other):
        x1, y1 = self.to_point()
        x2, y2 = other.to_point()
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
