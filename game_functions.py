import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond for key downs

    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullet and update group bullets
        if len(bullets) < ai_settings.bullets_allowed:
             new_bullet = Bullet(ai_settings, screen, ship)
             bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond for key ups """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Process touchs of buttom keyboard and mouse

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    """ Update positions of bullets and kill bullets than outside screen

    """
    #Update positions of bullets
    bullets.update()

    #Delete bullets than outside screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """Update screen and create a new screen

    """
    #For every step circle it refresh screen
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #Show the last screen
    pygame.display.flip()

