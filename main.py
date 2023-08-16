import sys
import pygame
from setting import Settings
from ship import Ship
import functions as gf
from pygame.sprite import Group
from enemy import Enemy

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space War")
    ship = Ship(ai_settings, screen)
    enemy = Group()
    missile = Group()
    current_time = pygame.time.get_ticks()
    next_move = current_time + 2000  # 1s = 1000ms
    while True:
        current_time = pygame.time.get_ticks()
        if next_move <= current_time:
            gf.enemy_gen(ai_settings, enemy, screen)
            next_move = current_time + 2000
        gf.check_event(ship, missile, ai_settings, screen)
        ship.update()
        enemy.update()
        gf.update_colli(missile, enemy, ai_settings)
        gf.missile_update(missile)
        gf.enemy_update(enemy)
        # gf.draw_text(screen, str(ai_settings.score), 18, 10, 10)
        gf.update_screen(ai_settings, screen, ship, missile, enemy)
run_game()



