from bullet import Bullet
import copy


class DoubleGun:

    def __init__(self, screen):
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
            bullets.append(Bullet(self.screen, point_copy))

        return bullets

