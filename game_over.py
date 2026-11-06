# Game Over screen for Alien Invasion game

import pygame
import pygame.font
from button import Button

class GameOver():
    """A class to show the Game Over screen with Restart and Quit buttons."""

    def __init__(self, settings, screen):
        """Initialize Game Over screen attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dark translucent layer drawn over the game.
        self.overlay = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        self.overlay.set_alpha(150)
        self.overlay.fill((0, 0, 0))

        # Render the "GAME OVER" title above the center of the screen.
        self.title_font = pygame.font.SysFont(None, 96)
        self.title_image = self.title_font.render("GAME OVER", True, (255, 0, 0))
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.bottom = self.screen_rect.centery - 40

        # Make the Restart button and move it to the left of the center.
        self.restart_button = Button(settings, screen, "Restart")
        self.restart_button.rect.centerx = self.screen_rect.centerx - 120
        self.restart_button.prep_msg("Restart")

        # Make the Quit button (red) and move it to the right of the center.
        self.quit_button = Button(settings, screen, "Quit")
        self.quit_button.button_color = (200, 0, 0)
        self.quit_button.rect.centerx = self.screen_rect.centerx + 120
        self.quit_button.prep_msg("Quit")

    def draw(self):
        """Draw the overlay, the title and both buttons."""
        self.screen.blit(self.overlay, (0, 0))
        self.screen.blit(self.title_image, self.title_rect)
        self.restart_button.draw_button()
        self.quit_button.draw_button()
