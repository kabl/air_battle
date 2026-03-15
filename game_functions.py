import sys
import pygame
from plane.missile import Missile
from explosion import Explosion


def check_events(game_stats, scoreboard, air_plane, enemies, sound_manager):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_stats, scoreboard, air_plane, enemies, sound_manager)
        elif event.type == pygame.KEYUP:
            check_keyup(event, air_plane)


def check_keydown(event, game_stats, scoreboard, air_plane, enemies, sound_manager):
    if event.key == pygame.K_RIGHT:
        air_plane.turn_right = True
    elif event.key == pygame.K_LEFT:
        air_plane.turn_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_stats, scoreboard, air_plane, sound_manager)
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


_GUN_SOUND_METHODS = ['play_simple_gun', 'play_double_gun', 'play_missile_launch']


def fire_bullet(game_stats, scoreboard, air_plane, sound_manager):
    air_plane.fire_bullet()
    game_stats.increment_shot_bullets()
    scoreboard.prep_hit_ratio()
    getattr(sound_manager, _GUN_SOUND_METHODS[air_plane.active_gun])()


def update_screen(screen, scoreboard, air_planes, enemies, backGround, explosions, game_over=False):
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

    for explosion in explosions:
        explosion.blitme()

    if game_over:
        _draw_game_over_banner(screen)

    pygame.display.flip()


def _draw_game_over_banner(screen):
    screen_rect = screen.get_rect()
    banner_w, banner_h = 500, 130
    overlay = pygame.Surface((banner_w, banner_h), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, overlay.get_rect(center=screen_rect.center))

    font = pygame.font.SysFont(None, 100)
    text = font.render('GAME OVER', True, (220, 50, 50))
    screen.blit(text, text.get_rect(center=screen_rect.center))


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


def update_bullets2(game_stats, scoreboard, base_planes, explosions, air_plane, sound_manager):
    cp_base_planes = base_planes.copy()
    for base_plane in base_planes:
        cp_base_planes.remove(base_plane)
        collisions = pygame.sprite.groupcollide(base_plane.bullets, cp_base_planes, True, True)
        if collisions:
            for bullet, targets in collisions.items():
                for target in targets:
                    sound_manager.play_crash_explosion()
                    if target is air_plane:
                        game_stats.game_over = True
                        game_stats.game_over_time = pygame.time.get_ticks()
                        sound_manager.play_player_hit()
                    else:
                        game_stats.increment_shot_enemies()
                        scoreboard.prep_score()
                if isinstance(bullet, Missile):
                    explosions.add(Explosion(scoreboard.screen, bullet.rect.center))
                    sound_manager.play_explosion()

        for missile in [b for b in base_plane.bullets if isinstance(b, Missile)]:
            missile.search_and_follow_target(cp_base_planes)

        cp_base_planes.add(base_plane)


# def check_collission(air_plane, enemies):
    # if pygame.sprite.spritecollideany(air_plane, enemies):
    #    print("Air plane hit!!! GAME OVER")

