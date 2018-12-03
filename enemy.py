import pygame
import game_functions as gf
from pygame.sprite import Sprite
import random
import copy

class Enemy(Sprite):
    def __init__(self, ai_settings, screen, point):
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.original_image = pygame.image.load("images/ship4.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.point = copy.copy(point)
        self.rect.x = self.point.x
        self.rect.y = self.point.y

        self.x = float(self.rect.x)
        self.counter = 0

        self.min = random.randint(0, 30) - 30
        self.max = random.randint(0, 30)
        self.speed = random.randint(1, 3)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.counter = self.counter + 1
        if self.counter % 10 == 0:
            x = random.randint(self.min, self.max)
            self.turn(x)

        self.drive(self.speed)

    def turn(self, delta):
        self.point.direction += delta
        self.image = pygame.transform.rotate(self.original_image, self.point.get_direction())
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def drive(self, speed):
        x1, y1 = self.point.move(speed)
        if gf.is_in_area(self.ai_settings, x1, y1):
            self.rect.center = (x1, y1)
        else:
            self.point.direction = self.point.direction - 180