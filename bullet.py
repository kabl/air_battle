import pygame
from pygame.sprite import Sprite
import copy


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, point):
        super(Bullet, self).__init__()
        self.screen = screen
        self.point = copy.copy(point)
        self.point.move(30)

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = point.x
        self.rect.top = point.y

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        x, y = self.point.move(self.speed_factor)
        self.rect.x = x
        self.rect.y = y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
