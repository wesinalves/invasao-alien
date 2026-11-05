import pygame


class Button:
    """Botao com destaque para mouse, teclado e controle."""

    def __init__(self, settings, screen, msg, y, width=300):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, width, 54)
        self.rect.center = (screen.get_rect().centerx, y)
        self.msg = msg
        self.font = pygame.font.SysFont('arial', 27, bold=True)

    def draw_button(self, selected=False):
        color = (25, 112, 78) if selected else (15, 38, 65)
        border = (110, 255, 177) if selected else (63, 111, 153)
        shadow = self.rect.move(0, 4)
        pygame.draw.rect(self.screen, (3, 12, 27), shadow, border_radius=12)
        pygame.draw.rect(self.screen, color, self.rect, border_radius=12)
        pygame.draw.rect(self.screen, border, self.rect, 2, border_radius=12)
        if selected:
            pygame.draw.rect(self.screen, (173, 255, 205), self.rect.inflate(8, 8), 1, border_radius=15)
        label = self.font.render(self.msg, True, (255, 255, 255))
        self.screen.blit(label, label.get_rect(center=self.rect.center))
