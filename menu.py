import pygame


class Menu:
    """Desenha o menu principal e as telas de informacoes."""

    def __init__(self, screen):
        self.screen = screen
        self.center_x = screen.get_rect().centerx
        self.title_font = pygame.font.SysFont('arial', 58, bold=True)
        self.heading_font = pygame.font.SysFont('arial', 40, bold=True)
        self.font = pygame.font.SysFont('arial', 23)
        self.small_font = pygame.font.SysFont('arial', 18)

    def text(self, message, y, font=None, color=(230, 242, 255)):
        font = font or self.font
        surface = font.render(message, True, color)
        self.screen.blit(surface, surface.get_rect(center=(self.center_x, y)))

    def panel(self):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((2, 9, 24, 120))
        pygame.draw.rect(overlay, (5, 20, 42, 218), (225, 48, 630, 510), border_radius=24)
        pygame.draw.rect(overlay, (57, 138, 168, 200), (225, 48, 630, 510), 2, border_radius=24)
        self.screen.blit(overlay, (0, 0))

    def draw_main_menu(self, buttons, selected):
        self.panel()
        self.text('INVASÃO ALIEN', 117, self.title_font, (115, 255, 170))
        self.text('DEFENDA A TERRA', 164, self.small_font, (172, 210, 240))
        for index, button in enumerate(buttons):
            button.draw_button(index == selected)
        self.text('SETAS / ANALÓGICO: NAVEGAR    |    ENTER / A: SELECIONAR',
                  530, self.small_font, (175, 202, 226))

    def draw_controls(self, back_button, selected=True):
        self.panel()
        self.text('CONTROLES', 120, self.heading_font, (115, 255, 170))
        self.text('TECLADO', 190, self.font, (130, 213, 255))
        self.text('Setas esquerda / direita: mover a nave', 229)
        self.text('Espaco: atirar    |    ESC: voltar ao menu', 265)
        self.text('CONTROLE', 325, self.font, (130, 213, 255))
        self.text('Analógico esquerdo / direcional: mover', 362)
        self.text('Botão A/X (principal): atirar    |    B/O: voltar', 398)
        self.text('Start: pausar e voltar ao menu', 433)
        back_button.draw_button(selected)

    def draw_about(self, back_button, selected=True):
        self.panel()
        self.text('SOBRE O JOGO', 122, self.heading_font, (115, 255, 170))
        self.text('INVASÃO ALIEN', 209, self.font, (130, 213, 255))
        self.text('Defenda sua nave de ondas de alienígenas.', 255)
        self.text('Ganhe pontos, avance de nível e sobreviva!', 295)
        self.text('Projeto de Programação Orientada a Objetos', 359)
        self.text('Desenvolvido em Python com Pygame', 396)
        back_button.draw_button(selected)
