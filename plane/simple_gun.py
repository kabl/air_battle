import copy
from plane.bullet2 import Bullet2

class SimpleGun:

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

    def fire(self, point):
        point_copy = copy.copy(point)
        point_copy.move(30)
        return Bullet2(self.ai_settings, self.screen, point_copy)

