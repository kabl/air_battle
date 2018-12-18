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
    number_of_enemies = ai_settings.start_enemies
    for x in range(number_of_enemies):
        enemies.add(Enemy(ai_settings, screen))

    clock = pygame.time.Clock()

    while True:
        clock.tick(100)
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        enemies.update()
        gf.update_bullets(ai_settings, bullets, enemies)
        gf.check_collission(ship, enemies)
        bullets.update()

        if len(enemies) == 0:
            number_of_enemies = number_of_enemies + 2
            for x in range(number_of_enemies):
                enemies.add(Enemy(ai_settings, screen))

        gf.update_screen(ai_settings, screen, ship, enemies, bullets)


run_game()
