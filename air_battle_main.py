import pygame
from pygame.sprite import Group
from settings import Settings
from plane.air_plane import AirPlane
from plane.enemy_plane import EnemyPlane
import game_functions as gf
from scoreboard import Scoreboard
from game_stats import GameStats


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def run_game():
    pygame.init()
    ai_settings = Settings()
    backGround = Background('images/background1.png', [0, 0])

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("GAME")
    game_stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, game_stats)
    air_plane = AirPlane(ai_settings, screen)

    enemies = Group()
    number_of_enemies = ai_settings.start_enemies
    for x in range(number_of_enemies):
        enemies.add(EnemyPlane(ai_settings, screen))

    clock = pygame.time.Clock()

    while True:
        clock.tick(100)
        gf.check_events(game_stats, scoreboard, air_plane)
        air_plane.update()
        enemies.update()
        gf.update_bullets(game_stats, scoreboard, air_plane.bullets, enemies)
        gf.check_collission(air_plane, enemies)

        if len(enemies) == 0:
            number_of_enemies = number_of_enemies + 2
            for x in range(number_of_enemies):
                enemies.add(EnemyPlane(ai_settings, screen))

        gf.update_screen(screen, scoreboard, air_plane, enemies, backGround)


run_game()
