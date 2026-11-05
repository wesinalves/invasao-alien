import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from menu import Menu
import game_functions as gf


def run_game():
    pygame.init()
    pygame.joystick.init()
    clock = pygame.time.Clock()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Invasao Alien')

    background = pygame.image.load('images/space.png').convert()
    background = pygame.transform.scale(background, screen.get_size())
    background_rect = background.get_rect()

    stats = GameStats(settings)
    scoreboard = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    menu = Menu(screen)

    buttons = [
        Button(settings, screen, 'JOGAR', 246),
        Button(settings, screen, 'CONTROLES', 316),
        Button(settings, screen, 'SOBRE', 386),
        Button(settings, screen, 'SAIR', 456),
    ]
    back_button = Button(settings, screen, 'VOLTAR', 495)

    current_screen = 'menu'
    selected = 0
    controller = None
    if pygame.joystick.get_count() > 0:
        controller = pygame.joystick.Joystick(0)
        controller.init()
    axis_direction = 0
    axis_last_move = 0

    def go_to_menu():
        nonlocal current_screen, selected
        current_screen = 'menu'
        selected = 0
        stats.game_active = False
        ship.moving_left = False
        ship.moving_right = False
        pygame.mouse.set_visible(True)

    def start_game():
        nonlocal current_screen
        # Reutiliza o inicio de partida original.
        gf.check_play_button(settings, screen, stats, scoreboard,
                             buttons[0], ship, aliens, bullets,
                             buttons[0].rect.centerx, buttons[0].rect.centery)
        current_screen = 'game'
        ship.moving_left = False
        ship.moving_right = False

    def activate():
        nonlocal current_screen
        if current_screen in ('controls', 'about'):
            current_screen = 'menu'
        elif current_screen == 'menu':
            if selected == 0:
                start_game()
            elif selected == 1:
                current_screen = 'controls'
            elif selected == 2:
                current_screen = 'about'
            elif selected == 3:
                pygame.quit()
                sys.exit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.JOYDEVICEADDED and controller is None:
                controller = pygame.joystick.Joystick(event.device_index)
                controller.init()
            elif event.type == pygame.JOYDEVICEREMOVED:
                controller = None
                axis_direction = 0
                ship.moving_left = False
                ship.moving_right = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if current_screen != 'menu':
                        go_to_menu()
                elif current_screen == 'menu':
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        selected = (selected + 1) % len(buttons)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        selected = (selected - 1) % len(buttons)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        activate()
                elif current_screen in ('controls', 'about'):
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        activate()
                elif current_screen == 'game':
                    gf.check_keydown_events(event, settings, screen, ship, bullets)

            elif event.type == pygame.KEYUP and current_screen == 'game':
                gf.check_keyup_events(event, ship)

            elif event.type == pygame.MOUSEMOTION and current_screen == 'menu':
                for index, button in enumerate(buttons):
                    if button.rect.collidepoint(event.pos):
                        selected = index
                        break

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == 'menu':
                    for index, button in enumerate(buttons):
                        if button.rect.collidepoint(event.pos):
                            selected = index
                            activate()
                            break
                elif current_screen in ('controls', 'about'):
                    if back_button.rect.collidepoint(event.pos):
                        activate()

            elif event.type == pygame.JOYHATMOTION:
                x, y = event.value
                if current_screen == 'menu':
                    if y > 0:
                        selected = (selected - 1) % len(buttons)
                    elif y < 0:
                        selected = (selected + 1) % len(buttons)
                elif current_screen == 'game':
                    ship.moving_left = x < 0
                    ship.moving_right = x > 0

            elif event.type == pygame.JOYAXISMOTION and event.axis == 0:
                direction = -1 if event.value < -0.5 else (1 if event.value > 0.5 else 0)
                if current_screen == 'menu':
                    now = pygame.time.get_ticks()
                    if direction != 0 and (direction != axis_direction or now - axis_last_move > 250):
                        selected = (selected + direction) % len(buttons)
                        axis_last_move = now
                elif current_screen == 'game':
                    ship.moving_left = direction < 0
                    ship.moving_right = direction > 0
                axis_direction = direction

            elif event.type == pygame.JOYBUTTONDOWN:
                # Mapeamento mais comum: A=0, B=1, Start=7 (alguns usam 6).
                if current_screen == 'menu':
                    if event.button in (0, 7, 6):
                        activate()
                elif current_screen in ('controls', 'about'):
                    if event.button in (0, 1, 6, 7):
                        activate()
                elif current_screen == 'game':
                    if event.button in (1, 6, 7):
                        go_to_menu()
                    elif event.button == 0:
                        gf.fire_bullet(settings, screen, ship, bullets)

        screen.blit(background, background_rect)

        if current_screen == 'menu':
            menu.draw_main_menu(buttons, selected)
        elif current_screen == 'controls':
            menu.draw_controls(back_button)
        elif current_screen == 'about':
            menu.draw_about(back_button)
        elif current_screen == 'game':
            if stats.game_active:
                ship.update()
                gf.update_bullets(settings, screen, stats, scoreboard, ship, aliens, bullets)
                gf.update_aliens(settings, stats, screen, scoreboard, ship, aliens, bullets)
            if stats.game_active:
                for bullet in bullets:
                    bullet.draw_bullet()
                ship.blitme()
                aliens.draw(screen)
                scoreboard.show_score()
            else:
                go_to_menu()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    run_game()
