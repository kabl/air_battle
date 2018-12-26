import sys
import pygame
from plane.missile import Missile


def check_events(game_stats, scoreboard, air_plane, enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_stats, scoreboard, air_plane, enemies)
        elif event.type == pygame.KEYUP:
            check_keyup(event, air_plane)


def check_keydown(event, game_stats, scoreboard, air_plane, enemies):
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
    elif event.key == pygame.K_e:
        for enemy in enemies:
            enemy.fire_bullet()


def check_keyup(event, air_plane):
    if event.key == pygame.K_RIGHT:
        air_plane.turn_right = False
    if event.key == pygame.K_LEFT:
        air_plane.turn_left = False


def fire_bullet(game_stats, scoreboard, air_plane):
    air_plane.fire_bullet()
    game_stats.increment_shot_bullets()
    scoreboard.prep_hit_ratio()


def update_screen(screen, scoreboard, air_planes, enemies, backGround):
    screen.fill((230, 230, 230))
   # screen.fill([255, 255, 255])
   # screen.blit(backGround.image, backGround.rect)

    scoreboard.show_score()
    scoreboard.show_hit_ratio()

    for air_plane in air_planes:
        air_plane.blitme()
        for bullet in air_plane.bullets:
            bullet.blitme()

    for enemy in enemies:
        enemy.blitme()
        for bullet in enemy.bullets:
            bullet.blitme()

    pygame.display.flip()


def update_bullets(game_stats, scoreboard, air_planes, enemies):
    for air_plane in air_planes:
        collisions = pygame.sprite.groupcollide(air_plane.bullets, enemies, True, True)
        if collisions:
            game_stats.increment_shot_enemies()
            scoreboard.prep_score()

        for missile in [b for b in air_plane.bullets if isinstance(b, Missile)]:
            missile.search_and_follow_target(enemies)

    for enemy in enemies:
        collisions2 = pygame.sprite.groupcollide(enemy.bullets, air_planes, True, True)
        if collisions2:
            print("GAME OVER!!!!")

        for missile in [b for b in enemy.bullets if isinstance(b, Missile)]:
            missile.search_and_follow_target(air_planes)


def update_bullets2(game_stats, scoreboard, base_planes):
    cp_base_planes = base_planes.copy()
    for base_plane in base_planes:
        cp_base_planes.remove(base_plane)
        print('update base_plane:', str(len(cp_base_planes)))
        collisions = pygame.sprite.groupcollide(base_plane.bullets, cp_base_planes, True, True)
        if collisions:
            game_stats.increment_shot_enemies()
            scoreboard.prep_score()
            print('collissions')

        for missile in [b for b in base_plane.bullets if isinstance(b, Missile)]:
            missile.search_and_follow_target(cp_base_planes)

        cp_base_planes.add(base_plane)


# def check_collission(air_plane, enemies):
    # if pygame.sprite.spritecollideany(air_plane, enemies):
    #    print("Air plane hit!!! GAME OVER")

