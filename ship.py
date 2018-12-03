import pygame
import math
import game_functions as gf
from point import Point

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

        x, y = self.rect.center
        self.point = Point(x, y, 0)

       # self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.drive_front = False
        self.direction = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.drive_front:
            self.drive(self.ai_settings.ship_speed_factor)
        if self.moving_right:
            self.turn(-self.ai_settings.ship_speed_rotation)
        if self.moving_left:
            self.turn(self.ai_settings.ship_speed_rotation)

    def turn(self, delta):
        self.direction += delta
        self.image = pygame.transform.rotate(self.original_image, self.get_direction())
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def get_direction(self):
        return self.direction % 360

    def drive(self, speed):

        x0, y0 = self.rect.center

        x1 = round(x0 + speed * math.cos((self.get_direction() + 90) * math.pi / 180))
        y1 = round(y0 + speed * math.sin((self.get_direction() - 90) * math.pi / 180))

        if gf.is_in_area(self.ai_settings, x1, y1):
            self.rect.center = (x1, y1)
