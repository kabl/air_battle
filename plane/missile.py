from plane.base_plane import BasePlane
import pygame
import copy
import math


class Missile(BasePlane):

    def __init__(self, ai_settings, screen, point):
        BasePlane.__init__(self,
                           ai_settings,
                           screen,
                           "images/missile1.png",
                           point)

        self.radius = 300
        self.circle_point = copy.copy(self.point)

    def update(self):
        self.drive(5)
        self.circle_point = copy.copy(self.point)
        self.circle_point.move(self.radius)

    def blitme(self):
        BasePlane.blitme(self)
        # color = 60, 60, 60
        color = 230, 230, 230
        # pygame.draw.circle(self.screen, color, self.circle_point.to_point(), self.radius, 2)

    def search_and_follow_target(self, targets):

        # 1st: check if the target is in the radar circle of the missile
        # in_circle_enemies = []
        targets_in_range = []
        for target in targets:
            distance = self.circle_point.distance_to(target.point)

            # 2nd: check all target distances from the missile which are in the radar
            if distance < self.radius:
                # in_circle_enemies.append(target)
                distance2 = self.point.distance_to(target.point)
                targets_in_range.append((distance2, target))

        # 3rd: select the closest target
        if len(targets_in_range) > 0:
            sorted_enemies = sorted(targets_in_range, key=lambda x: (x[0]))
            target = sorted_enemies[0][1]
            p1 = copy.copy(self.point)
            p1.turn(5)
            p1.move(5)
            d1 = p1.distance_to(target.point)

            p2 = copy.copy(self.point)
            p2.turn(-5)
            p2.move(5)
            d2 = p2.distance_to(target.point)

            dist_diff = math.fabs(d1 - d2)
            print("selected target: " + str(target) + ", dist diff: " + str(dist_diff))
            if d1 > d2:
                self.turn(-3 * dist_diff)
            elif d1 < d2:
                self.turn(3 * dist_diff)
