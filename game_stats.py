class GameStats():

    """"Track game statistics for Alien Invasion."""
    def __init__(self,ai_sitting):
        """Initialize statistics."""
        self.ai_sitting = ai_sitting
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_sitting.ship_limit
