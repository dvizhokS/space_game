import pygame, sys
from bullet import Bullet
from alien import Alien
import time


def events(screen, gun, bullets):
    """event handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # right
            if event.key == pygame.K_d:
                gun.mright = True
            # left
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # right
            if event.key == pygame.K_d:
                gun.mright = False
            # left
            elif event.key == pygame.K_a:
                gun.mleft = False
        # elif event.type == pygame.TEXTINPUT:
        #     if event.text == " ":
        #         new_bullet = Bullet(screen, gun)
        #         bullets.add(new_bullet)


def update(bg_color, screen, stats, sc, gun, aliens, bullets):
    """Update the background and screen"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets):
    """update bullet position"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += 10 * len(alien)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def create_army(screen, aliens):
    """Create an army aliens"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    space_width_alien = 0
    number_alien_x = int((700 - 2 * alien_width) / (alien_width + space_width_alien))
    alien_height = alien.rect.height
    number_alien_y = int((800 - 300 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width + space_width_alien) * alien_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)


def gun_kill(stats, screen, sc, gun, aliens, bullets):
    """Collide gun and aliens"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_aliens(stats, screen, sc, gun, aliens, bullets):
    """Update aliens positions"""
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, sc, gun, aliens, bullets)
    aliens_check(stats, screen, sc, gun, aliens, bullets)


def aliens_check(stats, screen, sc, gun, aliens, bullets):
    """Checking walk army position to bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, aliens, bullets)
            break


def check_high_score(stats, sc):
    """Check new record score"""
    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open("highscore.txt", "w") as f:
            f.write(str(stats.score))

