import pygame
from pygame.sprite import Group
from settings import Settings
from plane.air_plane import AirPlane
from plane.enemy_plane import EnemyPlane
import game_functions as gf
from scoreboard import Scoreboard
from game_stats import GameStats


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("GAME")
    game_stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, game_stats)
    ship = AirPlane(ai_settings, screen)
    #bullets = Group()

    enemies = Group()
    number_of_enemies = ai_settings.start_enemies
    for x in range(number_of_enemies):
        enemies.add(EnemyPlane(ai_settings, screen))

    clock = pygame.time.Clock()

    while True:
        clock.tick(100)
        gf.check_events(game_stats, scoreboard, ship)
        ship.update()
        enemies.update()
        gf.update_bullets(game_stats, scoreboard, ship.bullets, enemies)
        gf.check_collission(ship, enemies)

        if len(enemies) == 0:
            number_of_enemies = number_of_enemies + 2
            for x in range(number_of_enemies):
                enemies.add(EnemyPlane(ai_settings, screen))

        gf.update_screen(ai_settings, screen, scoreboard, ship, enemies)


run_game()
