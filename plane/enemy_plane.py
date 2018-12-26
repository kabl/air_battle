import random
from pygame.sprite import Group
from plane.base_plane import BasePlane
from plane.missile_gun import MissileGun


class EnemyPlane(BasePlane):

    def __init__(self, ai_settings, screen):
        BasePlane.__init__(self, ai_settings, screen, "images/ship6small.png")

        self.min = random.randint(0, 30) - 30
        self.max = random.randint(0, 30)
        self.speed = random.randint(1, 3)
        self.counter = 0

        self.bullets = Group()
        self.gun = MissileGun(ai_settings, screen)

    def fire_bullet(self):
        new_bullets = self.gun.fire(self.point)
        self.bullets.add(new_bullets)

    def update(self):
        self.counter = self.counter + 1
        if self.counter % 10 == 0:
            x = random.randint(self.min, self.max)
            self.turn(x)

        self.drive(self.speed)
        self.bullets.update()

