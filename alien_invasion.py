# Python Journey - Chapter 32
# Creating a Pygame Window and Responding to User Input for Alien Invasion project

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from game_over import GameOver
clock = pygame.time.Clock()

def run_game():
    '''Main function of Alien Invasion game'''
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    background_image = pygame.image.load('images/space.png')
    background_image = pygame.transform.scale(background_image, (ai_settings.screen_width, ai_settings.screen_height))
    background_rect = background_image.get_rect()
    background_rect.topleft = (0, 0)

    # Make a play button
    play_button = Button(ai_settings, screen, "Play")

    # Make the Game Over screen (Restart and Quit buttons)
    game_over_screen = GameOver(ai_settings, screen)

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make a group to store Aliens in..
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, game_over_screen)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)       
        
        gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets, play_button, background_image, background_rect, game_over_screen)
        clock.tick(60)
run_game()
