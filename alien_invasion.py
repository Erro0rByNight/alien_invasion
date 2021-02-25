import sys
import pygame
from pygame.sprite import Group

from sitting import *
from ship import *
import game_functions as gf
#######################

def run_game():
    # Initialize game and create screen object.
    pygame.init()
    ai_sitting = Sitting()
    screen = pygame.display.set_mode((
        ai_sitting.screen_width,ai_sitting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Set the background color.
    bg_color = (ai_sitting.bg_color)

    # Make a ship.
    ship = Ship(ai_sitting,screen)
    #Make a group to store bullets in.
    bullets = Group()

    #

    bg_color = (ai_sitting.bg_color)

    # Make a ship.
    ship = Ship(ai_sitting,screen)
    #Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_sitting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_sitting,screen,ship,bullets)



run_game()
