import pygame
import math
import game_functions as gf


class Ship():

    def __init__(self, ai_seettings, screen):
        self.ai_settings = ai_seettings
        self.screen = screen
        self.original_image = pygame.image.load("images/ship4.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.drive_front = False
        self.direction = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.drive_front:
            self.drive()
        if self.moving_right:
            self.turn(-1)
        if self.moving_left:
            self.turn(1)

    def turn(self, directoin):
        self.direction += directoin
        self.image = pygame.transform.rotate(self.original_image, self.get_direction())
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def get_direction(self):
        return self.direction % 360

    def drive(self):

        # new_x = x + distance * Math.Cos(angle_degrees * Math.Pi / 180)
        # new_y = y + distance * Math.Sin(angle_degrees * Math.Pi / 180)

        x0, y0 = self.rect.center

        x1 = round(x0 + 3 * math.cos((self.get_direction() + 90) * math.pi / 180))
        y1 = round(y0 + 3 * math.sin((self.get_direction() - 90) * math.pi / 180))
        diff = x1 - x0
        direction = "none"
        if diff > 0:
            direction = "right"
        elif diff < 0:
            direction = "left"

        print("X direction: " + direction + ", diff: " + str(diff) + ", pos: " + str(x1))

        if gf.is_in_area(self.ai_settings, x1, y1):
            self.rect.center = (x1, y1)
        else:
            print("Not in area")
