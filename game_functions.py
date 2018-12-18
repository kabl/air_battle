import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def check_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.drive_front = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, ship):
    if event.key == pygame.K_UP:
        ship.drive_front = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, enemies, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    for enemy in enemies:
        enemy.blitme()

    pygame.display.flip()


def update_bullets(ai_settings, bullets, enemies):
    for bullet in bullets.copy():
        if not is_in_area(ai_settings, bullet.point.x, bullet.point.y):
            bullets.remove(bullet)

    #print("Bullet size:", len(bullets))

    collissions = pygame.sprite.groupcollide(bullets, enemies, True, True)


def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship.point)
    bullets.add(new_bullet)


def check_collission(ship, enemies):
    if pygame.sprite.spritecollideany(ship, enemies):
        print("Ship hit!!! GAME OVER")


def is_in_area(ai_settings, x, y):
    return x >= 0 \
        and x <= ai_settings.screen_width \
        and y >= 0 \
        and y <= ai_settings.screen_height
