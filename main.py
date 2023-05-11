import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    screen_size = (700, 800)

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Space war")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, gun, aliens, bullets)
        clock.tick(60)


run()

