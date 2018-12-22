from bullet import Bullet
import copy


class SimpleGun:

    def __init__(self, screen):
        self.screen = screen

    def fire(self, point):
        point2 = copy.copy(point)
        point2.move(30)
        return Bullet(self.screen, point2)

