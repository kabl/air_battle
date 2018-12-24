from plane.base_plane import BasePlane


class Bullet2(BasePlane):

    def __init__(self, ai_settings, screen, point):
        BasePlane.__init__(self,
                           ai_settings,
                           screen,
                           "images/bullet1.png",
                           point)

    def update(self):
        self.drive(8)
       # BasePlane.update(self)
