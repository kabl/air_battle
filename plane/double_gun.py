import copy
from plane.bullet2 import Bullet2


class DoubleGun:

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

    def fire(self, point):

        movements = [20, -20]
        bullets = []
        for movement in movements:
            point_copy = copy.copy(point)
            point_copy.move(30)
            point_copy.direction += 90
            point_copy.move(movement)
            point_copy.direction -= 90
            bullets.append(Bullet2(self.ai_settings, self.screen, point_copy))

        return bullets

