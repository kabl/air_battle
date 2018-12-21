import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import game_functions as gf
from point import Point
from bullet import Bullet


class BasePlane(Sprite):

    def __init__(self, ai_settings, screen, image_path):
        super(BasePlane, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.original_image = pygame.image.load(image_path)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        x, y = self.rect.center
        self.point = Point(x, y, 0)

        self.bullets = Group()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def turn(self, delta):
        self.point.direction += delta
        self.image = pygame.transform.rotate(self.original_image, self.point.get_direction())
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def drive(self, speed):
        x1, y1 = self.point.move(speed)
        if self.point.is_in_area(self.ai_settings):
            self.rect.center = (x1, y1)
        else:
            self.point.direction = self.point.direction - 180

    def fire_bullet(self, bullets):
        new_bullet = Bullet(self.ai_settings, self.screen, self.point)
        bullets.add(new_bullet)

    def update(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if not bullet.point.is_in_area(self.ai_settings):
                self.bullets.remove(bullet)
