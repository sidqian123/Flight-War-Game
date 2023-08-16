import pygame.image


class Settings:
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('/Users/sidqian/Documents/Sid/2021'
                                          '/coding/pythonProject1/venv/images/bg_image.jpeg')
        self.score = 0
        self.ship_speed = 3
        self.enemy_amount = 2
        self.missile_image = pygame.image.load('/Users/sidqian/Documents/Sid/2'
                                               '021/coding/pythonProject1/venv/images/missile.png')
        self.enemy_image = pygame.image.load('/Users/sidqian/Documents/'
                                             'Sid/2021/coding/pythonProject1/venv/images/enemy.png')
