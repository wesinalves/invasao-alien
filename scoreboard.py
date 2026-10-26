import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    def __init__(self, screen, stats):
        # Create an instance to store game statistics and create a scoreboard.
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

    def prep_score(self):
        # Turn the score into a rendered image and place it at the top right.
        score_str = str(int(self.stats.score))
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        # Turn the high score into a rendered image and center it at the top.
        high_score_str = str(int(self.stats.high_score))
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        # Turn the level into a rendered image and place it below the score.
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 60

    def prep_ships(self):
        # Show how many ships are left, at the top left of the screen.
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
