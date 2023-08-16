import random
import pygame.image
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = ai_settings.enemy_image
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.y = -5
        self.rect.x = random.randint(0, 460)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += 1
