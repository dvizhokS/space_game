import pygame


class Alien(pygame.sprite.Sprite):
    """Class one Alien"""

    def __init__(self, screen):
        """Initialize and make coordinates"""
        super(Alien, self).__init__()
        sizes = (50, 50)
        self.screen = screen
        self.image = pygame.image.load("images/alien.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, sizes)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Draw the Alien on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move to spaceship"""
        self.y += 0.1
        self.rect.y = self.y

