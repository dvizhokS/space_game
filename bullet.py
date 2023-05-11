import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """create a bullet in gun position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 255, 255, 255
        self.speed = 4
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet in the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
