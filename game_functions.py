import sys
import pygame
from plane.simple_gun import SimpleGun
from plane.double_gun import DoubleGun
import os
from plane.missile import Missile

def check_events(game_stats, scoreboard, air_plane):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_stats, scoreboard, air_plane)
        elif event.type == pygame.KEYUP:
            check_keyup(event, air_plane)


def check_keydown(event, game_stats, scoreboard, air_plane):
    if event.key == pygame.K_RIGHT:
        air_plane.turn_right = True
    elif event.key == pygame.K_LEFT:
        air_plane.turn_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_stats, scoreboard, air_plane)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_1:
        air_plane.active_gun = 0
    elif event.key == pygame.K_2:
        air_plane.active_gun = 1
    elif event.key == pygame.K_3:
        air_plane.active_gun = 2


def check_keyup(event, air_plane):
    if event.key == pygame.K_RIGHT:
        air_plane.turn_right = False
    if event.key == pygame.K_LEFT:
        air_plane.turn_left = False


def update_screen(screen, scoreboard, air_plane, enemies, backGround):
    screen.fill((230, 230, 230))
   # screen.fill([255, 255, 255])
   # screen.blit(backGround.image, backGround.rect)

    scoreboard.show_score()
    scoreboard.show_hit_ratio()

    for bullet in air_plane.bullets:
        #  if "draw_bullet" in dir(bullet):
        #      bullet.draw_bullet()
        #  elif "blitme" in dir(bullet):
        bullet.blitme()

    air_plane.blitme()

    for enemy in enemies:
        enemy.blitme()

    pygame.display.flip()


def update_bullets(game_stats, scoreboard, bullets, enemies):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        game_stats.increment_shot_enemies()
        scoreboard.prep_score()

    for missile in [b for b in bullets if isinstance(b, Missile)]:
        missile.check_targets(enemies)

def fire_bullet(game_stats, scoreboard, air_plane):
    air_plane.fire_bullet()
    game_stats.increment_shot_bullets()
    scoreboard.prep_hit_ratio()


def check_collission(air_plane, enemies):
    if pygame.sprite.spritecollideany(air_plane, enemies):
        print("Air plane hit!!! GAME OVER")

