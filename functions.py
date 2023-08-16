import sys

import pygame
from missile import Missile
from enemy import Enemy


def check_keydown_event(event, ship, missile, ai_settings, screen):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_missile = Missile(ai_settings, screen, ship)
        missile.add(new_missile)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def enemy_gen(ai_settings, enemy, screen):
    # current_time = pygame.time.get_ticks()
    # next_move = current_time + 1000
    # while True:
    #     current_time = pygame.time.get_ticks()
    #     if next_move <= current_time:
    for i in range(ai_settings.enemy_amount):
        new_enemy = Enemy(ai_settings, screen)
        enemy.add(new_enemy)
        # next_move = current_time + 1000


def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()


def check_event(ship, missile, ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, missile, ai_settings, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, missile, enemy):
    screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, (0, 0))
    for missile in missile.sprites():
        missile.shoot()
    for enemy in enemy.sprites():
        enemy.blitme()

    ship.blitme()
    pygame.display.flip()


def missile_update(missile):
    missile.update()
    for missiles in missile.copy():
        if missiles.rect.bottom <= 0:
            missiles.remove()


def enemy_update(enemy):
    enemy.update()
    for enemies in enemy.copy():
        if enemies.rect.bottom <= 0:
            enemies.remove()


def update_colli(missile, enemy, ai_setting):
    collision = pygame.sprite.groupcollide(missile, enemy, True, True)
    if collision:
        missile.remove()
        enemy.remove()
        ai_setting.score += 1


# font_name = pygame.font.match_font('arial')
#
#
# def draw_text(surf, text, size, x, y):
#     font = pygame.font.Font(font_name, size)
#     text_surface = font.render(text, True, )
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     surf.blit(text_surface, text_rect)
