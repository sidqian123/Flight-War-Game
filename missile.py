import pygame.image
from pygame.sprite import Sprite
from pygame.math import Vector2

class Missile(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Missile, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = ai_settings.missile_image
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def shoot(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y -= 1
        self.rect.y = self.y


