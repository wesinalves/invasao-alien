class GameStats:
    """Acompanha as estatísticas do jogo Alien Invasion."""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1