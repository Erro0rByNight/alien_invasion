class Sitting():
    """ A class to store all sitting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's sitting."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,191,255)

        # Ship Sittings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet sittings
        self.bullet_speed_factor = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0,0,128
        self.bullet_allowed = 6

        # Alien settings
        self.alien_speed_factor = 0.8
        self.fleet_drop_speed = 8
        # fleet_direction of 1 represents right ; -1 represents left.
        self.fleet_direction = 1
