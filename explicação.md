# Invasão Alien
Projeto da disciplina de Programação Orientada a Objetos — CEUB. O objetivo é implementar o jogo Invasão Alien usando Pygame.

---

## Alunos:
- Lucas Puglise de Carvalho | 22603235
- João Paulo Torrano Lima | 22601922
- Arthur de Miranda | 22612297
- Miguel Soares Flores | 22601847
- Tiago Cordeiro | 22604732

---

## 🆕 Atividade: Tela de Game Over (Grupo — Lucas Puglise)

Foi adicionada uma tela de **Game Over** ao jogo, exibida automaticamente ao final de uma partida. Ela sobrepõe o cenário com uma camada escura semitransparente, apresenta o título "GAME OVER" em vermelho e dois botões lado a lado: **Restart** (reinicia a partida) e **Quit** (fecha o jogo).

### Arquivos criados

#### `game_over.py` *(novo)*

Contém a classe `GameOver`, responsável por toda a lógica visual da tela de derrota.

```python
class GameOver():
    def __init__(self, settings, screen): ...
    def draw(self): ...
```

| Atributo / método | Descrição |
|---|---|
| `self.overlay` | `pygame.Surface` semitransparente (alpha 150) que escurece o jogo ao fundo |
| `self.title_font` | Fonte de tamanho 96 para o título "GAME OVER" |
| `self.title_image` | Texto "GAME OVER" renderizado em vermelho `(255, 0, 0)` |
| `self.title_rect` | Centralizado horizontalmente, posicionado **acima** do centro vertical da tela |
| `self.restart_button` | Instância de `Button` (verde), deslocada **120 px à esquerda** do centro |
| `self.quit_button` | Instância de `Button` (vermelho `(200, 0, 0)`), deslocada **120 px à direita** do centro |
| `draw()` | Desenha a overlay, o título e os dois botões em cada frame |

---

### Arquivos modificados

#### `game_stats.py`

Adicionado um novo atributo de estado para controlar se a partida terminou em derrota, separando esse estado do simples "jogo inativo" (que também ocorre na tela inicial).

```python
# Antes
self.game_active = False

# Depois
self.game_active = False
self.game_over = False   # ← ADICIONADO: True somente após perder todas as naves
```

---

#### `game_functions.py`

**1. `ship_hit()` — ativa o estado de Game Over**

Quando o jogador perde a última nave (`ships_left == 0`), além de já definir `game_active = False`, agora também define `game_over = True`.

```python
# Antes
else:
    stats.game_active = False
    pygame.mouse.set_visible(True)

# Depois
else:
    stats.game_active = False
    stats.game_over = True          # ← ADICIONADO
    pygame.mouse.set_visible(True)
```

**2. `check_play_button()` — reseta o estado de Game Over ao reiniciar**

Ao iniciar uma nova partida (pelo botão Play ou pelo botão Restart), `game_over` volta a `False`.

```python
# Linha adicionada dentro do bloco `if button_clicked and not stats.game_active`:
stats.game_over = False             # ← ADICIONADO
```

**3. `check_game_over_buttons()` — nova função**

Verifica qual botão da tela de Game Over foi clicado e age de acordo.

```python
def check_game_over_buttons(settings, screen, stats, sb, play_button,
                             game_over_screen, ship, aliens, bullets,
                             mouse_x, mouse_y):
    """Restart or quit the game when the player clicks a Game Over button."""
    if game_over_screen.restart_button.rect.collidepoint(mouse_x, mouse_y):
        # Reuse the Play button logic to start a new game.
        check_play_button(settings, screen, stats, sb, play_button,
                          ship, aliens, bullets,
                          play_button.rect.centerx, play_button.rect.centery)
    elif game_over_screen.quit_button.rect.collidepoint(mouse_x, mouse_y):
        sys.exit()
```

**4. `check_events()` — trata cliques durante o Game Over**

Adicionado um novo ramo `elif` que intercepta eventos de clique do mouse enquanto `stats.game_over` é verdadeiro, antes do ramo que trataria o botão Play, evitando conflitos.

```python
# Ramo ADICIONADO (vem antes do elif MOUSEBUTTONDOWN original):
elif event.type == pygame.MOUSEBUTTONDOWN and stats.game_over:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    check_game_over_buttons(settings, screen, stats, sb, play_button,
                            game_over_screen, ship, aliens, bullets,
                            mouse_x, mouse_y)

# Assinatura da função também recebeu o novo parâmetro:
def check_events(..., game_over_screen):   # ← game_over_screen ADICIONADO
```

**5. `update_screen()` — desenha a tela de Game Over quando necessário**

A lógica que decide o que mostrar quando o jogo não está ativo foi ajustada para priorizar a tela de Game Over sobre o botão Play.

```python
# Antes
if not stats.game_active:
    play_button.draw_button()

# Depois
if stats.game_over:                    # ← bloco ADICIONADO
    game_over_screen.draw()
elif not stats.game_active:            # ← "if" virou "elif"
    play_button.draw_button()

# Assinatura da função também recebeu o novo parâmetro:
def update_screen(..., game_over_screen):   # ← game_over_screen ADICIONADO
```

---

#### `alien_invasion.py`

**1. Import da nova classe**

```python
from game_over import GameOver          # ← ADICIONADO
```

**2. Instanciação do objeto `GameOver`**

```python
# Make the Game Over screen (Restart and Quit buttons)
game_over_screen = GameOver(ai_settings, screen)   # ← ADICIONADO
```

**3. Chamadas atualizadas com o novo parâmetro**

As duas funções que receberam o parâmetro `game_over_screen` passam a recebê-lo nas chamadas do loop principal:

```python
# check_events
gf.check_events(ai_settings, screen, stats, sb, play_button,
                ship, aliens, bullets, game_over_screen)   # ← game_over_screen ADICIONADO

# update_screen
gf.update_screen(ai_settings, stats, screen, sb, ship, aliens, bullets,
                 play_button, background_image, background_rect,
                 game_over_screen)                          # ← game_over_screen ADICIONADO
```

---

## 📋 Resumo das mudanças

| Arquivo | Tipo | O que mudou |
|---|---|---|
| `game_over.py` | **Criado** | Classe `GameOver` com overlay, título e botões Restart/Quit |
| `game_stats.py` | Modificado | Novo atributo `game_over = False` |
| `game_functions.py` | Modificado | `ship_hit` ativa `game_over`; `check_play_button` reseta `game_over`; nova função `check_game_over_buttons`; `check_events` e `update_screen` recebem `game_over_screen` e tratam o novo estado |
| `alien_invasion.py` | Modificado | Import e instanciação de `GameOver`; passagem do parâmetro `game_over_screen` para `check_events` e `update_screen` |

---

## Como jogar

| Ação | Tecla / Controle |
|---|---|
| Mover para a direita | `→` |
| Mover para a esquerda | `←` |
| Atirar | `Espaço` |
| Sair do jogo | `Q` |
| Iniciar partida | Clique em **Play** |
| Reiniciar após derrota | Clique em **Restart** |
| Fechar após derrota | Clique em **Quit** |

---

## Pré-requisitos

```bash
pip install pygame
```

## Como executar

```bash
python alien_invasion.py
```

---

## Como contribuir

- Dê uma **estrela** (*Star*) neste repositório.
- Na página do repositório [POO](https://github.com/wesinalves/invasao-alien), clique no botão **Fork**.

```bash
git clone https://github.com/<seu-nome-de-usuario-no-github>/invasao-alien.git
```

Antes de fazer qualquer alteração, [mantenha seu *fork* sincronizado](https://www.freecodecamp.org/news/how-to-sync-your-fork-with-the-original-git-repository/):

```bash
git remote add upstream https://github.com/wesinalves/invasao-alien.git
git fetch upstream
git pull upstream master
git push
```

Mude para uma nova branch de desenvolvimento:

```bash
git checkout -b <nome-da-branch>
```

Adicione e faça commit das alterações:

```bash
git add -A
git commit -m "<sua-mensagem>"
git push origin <nome-da-branch>
```

Em seguida, crie um **Pull Request** na página do GitHub do seu fork.

---

## Referências

- [Documentação do Pygame](https://pyga.me/docs/)
