import pygame
from pygame.sprite import Sprite
import copy


class Bullet(Sprite):
    def __init__(self, screen, point):
        super(Bullet, self).__init__()

        self.bullet_speed_factor = 6
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60

        self.screen = screen
        self.point = point

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centerx = point.x
        self.rect.top = point.y

    def update(self):
        x, y = self.point.move(self.bullet_speed_factor)
        self.rect.x = x
        self.rect.y = y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
