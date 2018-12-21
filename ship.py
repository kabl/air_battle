from base_plane import BasePlane


class Ship(BasePlane):

    def __init__(self, ai_seettings, screen):
        BasePlane.__init__(self, ai_seettings, screen, "images/ship4small.png")

        self.moving_right = False
        self.moving_left = False
        self.drive_front = True

    def update(self):
        if self.drive_front:
            self.drive(self.ai_settings.ship_speed_factor)
        if self.moving_right:
            self.turn(-self.ai_settings.ship_speed_rotation)
        if self.moving_left:
            self.turn(self.ai_settings.ship_speed_rotation)

        BasePlane.update(self)
