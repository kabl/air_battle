from plane.base_plane import BasePlane


class AirPlane(BasePlane):

    def __init__(self, ai_settings, screen):
        BasePlane.__init__(self, ai_settings, screen, "images/ship4small.png")

        self.turn_right = False
        self.turn_left = False
        self.drive_front = True

    def update(self):
        if self.drive_front:
            self.drive(self.ai_settings.air_plane_speed_factor)
        if self.turn_right:
            self.turn(-self.ai_settings.air_plane_speed_rotation)
        if self.turn_left:
            self.turn(self.ai_settings.air_plane_speed_rotation)

        BasePlane.update(self)
