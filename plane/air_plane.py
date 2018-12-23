from plane.base_plane import BasePlane
from pygame.sprite import Group
from plane.simple_gun import SimpleGun
from plane.double_gun import DoubleGun
from plane.missile_gun import MissileGun

class AirPlane(BasePlane):

    def __init__(self, ai_settings, screen):
        BasePlane.__init__(self, ai_settings, screen, "images/plane2.png")

        self.turn_right = False
        self.turn_left = False
        self.drive_front = True

        self.bullets = Group()
        self.gun = [SimpleGun(screen),
                    DoubleGun(screen),
                    MissileGun(ai_settings, screen)]
        self.active_gun = 0

    def fire_bullet(self):
        new_bullets = self.gun[self.active_gun].fire(self.point)
        self.bullets.add(new_bullets)

    def update(self):
        if self.drive_front:
            self.drive(self.ai_settings.air_plane_speed_factor)
        if self.turn_right:
            self.turn(-self.ai_settings.air_plane_speed_rotation)
        if self.turn_left:
            self.turn(self.ai_settings.air_plane_speed_rotation)

        self.bullets.update()
        for bullet in self.bullets.copy():
            if not bullet.point.is_in_area(self.ai_settings):
                self.bullets.remove(bullet)
