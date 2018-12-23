import copy
from plane.missile import Missile


class MissileGun():

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        self.last_gun = 0

    def fire(self, point):

        movements = [20, -20]
        self.last_gun += 1
        point_copy = copy.copy(point)
        point_copy.direction += 90
        point_copy.move(movements[self.last_gun % 2])
        point_copy.direction -= 90

        return Missile(self.ai_settings, self.screen, point_copy)
