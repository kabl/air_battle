import sys
import pygame


def check_events(game_stats, scoreboard, ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_stats, scoreboard, ship)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def check_keydown(event, game_stats, scoreboard, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_stats, scoreboard, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, scoreboard, ship, enemies):
    screen.fill(ai_settings.bg_color)

    scoreboard.show_score()
    scoreboard.show_hit_ratio()

    for bullet in ship.bullets:
        bullet.draw_bullet()

    ship.blitme()

    for enemy in enemies:
        enemy.blitme()

    pygame.display.flip()


def update_bullets(game_stats, scoreboard, bullets, enemies):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        game_stats.increment_shot_enemies()
        scoreboard.prep_score()


def fire_bullet(game_stats, scoreboard, ship):
    ship.fire_bullet()
    game_stats.increment_shot_bullets()
    scoreboard.prep_hit_ratio()


def check_collission(ship, enemies):
    if pygame.sprite.spritecollideany(ship, enemies):
        print("Ship hit!!! GAME OVER")

