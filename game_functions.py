import sys
import pygame


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
        air_plane.moving_right = True
    elif event.key == pygame.K_LEFT:
        air_plane.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_stats, scoreboard, air_plane)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, air_plane):
    if event.key == pygame.K_RIGHT:
        air_plane.moving_right = False
    if event.key == pygame.K_LEFT:
        air_plane.moving_left = False


def update_screen(ai_settings, screen, scoreboard, air_plane, enemies):
    screen.fill(ai_settings.bg_color)

    scoreboard.show_score()
    scoreboard.show_hit_ratio()

    for bullet in air_plane.bullets:
        bullet.draw_bullet()

    air_plane.blitme()

    for enemy in enemies:
        enemy.blitme()

    pygame.display.flip()


def update_bullets(game_stats, scoreboard, bullets, enemies):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        game_stats.increment_shot_enemies()
        scoreboard.prep_score()


def fire_bullet(game_stats, scoreboard, air_plane):
    air_plane.fire_bullet()
    game_stats.increment_shot_bullets()
    scoreboard.prep_hit_ratio()


def check_collission(air_plane, enemies):
    if pygame.sprite.spritecollideany(air_plane, enemies):
        print("Air plane hit!!! GAME OVER")

