import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from enemy import Enemy
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("GAME")

    ship = Ship(ai_settings, screen)
    bullets = Group()

    enemies = Group()
    enemies.add(Enemy(ai_settings, screen, ship.point))
    enemies.add(Enemy(ai_settings, screen, ship.point))
    enemies.add(Enemy(ai_settings, screen, ship.point))
    enemies.add(Enemy(ai_settings, screen, ship.point))
    enemies.add(Enemy(ai_settings, screen, ship.point))

    clock = pygame.time.Clock()

    while True:
        clock.tick(100)
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        enemies.update()
        gf.update_bullets(bullets, enemies)
        bullets.update()

        gf.update_screen(ai_settings, screen, ship, enemies, bullets)


run_game()
