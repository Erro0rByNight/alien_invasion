import sys

import pygame
from bullet import Bullet

def check_keydown_events(event,ai_sitting,screen,ship,bullets):

    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_sitting,screen,ship,bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_sitting,screen,ship,bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_sitting.bullet_allowed:
        new_bullet = Bullet(ai_sitting,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_sitting,screen,ship,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_sitting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def update_screen(ai_sitting,screen,ship,bullets):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_sitting.bg_color)

    #Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()


    # Make the most recently drawn screen visibe.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and git rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that disappared.
    for  bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
