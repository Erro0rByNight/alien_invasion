class Sitting():
    """ A class to store all sitting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's sitting."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,51)

        # Ship Sittings
        self.ship_speed_factor = 1.5

        #Bullet sittings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
