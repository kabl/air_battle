import pygame
from pygame.sprite import Group
from settings import Settings
from plane.air_plane import AirPlane
from plane.enemy_plane import EnemyPlane
import game_functions as gf
from scoreboard import Scoreboard
from game_stats import GameStats
from main_menu import MainMenu, _StartGame
from sound_manager import SoundManager


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def play_game(screen, ai_settings, sound_manager):
    backGround = Background('images/background1.png', [0, 0])
    game_stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, game_stats)

    explosions = Group()

    air_plane = AirPlane(ai_settings, screen, explosions)
    air_planes = Group()
    air_planes.add(air_plane)

    enemies = Group()
    number_of_enemies = 2  # ai_settings.start_enemies
    for x in range(number_of_enemies):
        enemy = EnemyPlane(ai_settings, screen, explosions)
        enemies.add(enemy)

    base_planes = Group()
    base_planes.add(air_planes)
    base_planes.add(enemies)
    clock = pygame.time.Clock()
    sound_manager.start_music()

    counter = 0
    while True:
        clock.tick(70)
        gf.check_events(game_stats, scoreboard, air_plane, enemies, sound_manager)
        air_planes.update()
        enemies.update()
        explosions.update()
        # gf.update_bullets(game_stats, scoreboard, air_planes, enemies)
        gf.update_bullets2(game_stats, scoreboard, base_planes, explosions, air_plane, sound_manager)

        if game_stats.game_over:
            elapsed = pygame.time.get_ticks() - game_stats.game_over_time
            if elapsed >= 3000:
                sound_manager.stop_music()
                break

        if len(enemies) == 0:
            #number_of_enemies = number_of_enemies + 2
            for x in range(number_of_enemies):
                enemy = EnemyPlane(ai_settings, screen, explosions)
                enemies.add(enemy)
                base_planes.add(enemy)

        counter += 1
        if counter % 100000:
           pass
           # enemy.fire_bullet()

        gf.update_screen(screen, scoreboard, air_planes, enemies, backGround, explosions,
                         game_stats.game_over)


def run_game():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Air Battle")

    sound_manager = SoundManager()
    menu = MainMenu(screen)
    message = None
    while True:
        sound_manager.start_menu_music()
        try:
            menu.run(message)
        except _StartGame:
            sound_manager.stop_menu_music()
            play_game(screen, ai_settings, sound_manager)
            message = 'GAME OVER'


run_game()
