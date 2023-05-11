import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        """initialize Gun"""
        super(Gun, self).__init__()
        sizes = (80, 80)
        self.speed = 1
        self.mright = False
        self.mleft = False
        self.screen = screen
        self.image = pygame.image.load('images/space_ship.png')
        self.image = pygame.transform.scale(self.image, sizes)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """draw the gun"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """update the gun"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        elif self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= self.speed

        self.rect.centerx = self.center

    def create_gun(self):
        """gun position on center"""
        self.center = self.screen_rect.centerx
