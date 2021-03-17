import sys
import pygame
from pygame.sprite import Group

from sitting import *
from game_stats import GameStats
from ship import *
from alien import Alien
import game_functions as gf
#######################

def run_game():
    # Initialize game and create screen object.
    pygame.init()
    ai_sitting = Sitting()
    screen = pygame.display.set_mode((
        ai_sitting.screen_width,ai_sitting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_sitting)

    #Set the background color.
    bg_color = (ai_sitting.bg_color)

    # Make an Alien.
    alien = Alien(ai_sitting, screen)

    # Make a ship.
    ship = Ship(ai_sitting,screen)
    #Make a group to store bullets in.
    bullets = Group()

    #

    bg_color = (ai_sitting.bg_color)

    # Make a ship,a group to store bullets, a group of aliens.
    ship = Ship(ai_sitting,screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_sitting,screen,ship,aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_sitting,screen,ship,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_sitting,screen,ship,aliens,bullets)
            gf.update_aliens(ai_sitting,stats,screen,ship,aliens,bullets)
        
        gf.update_screen(ai_sitting,screen,ship,bullets,aliens)



run_game()
