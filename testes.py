import pygame
import pygame_gui
import time

pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definindo a janela do pygame
WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Criando um gerenciador de eventos pygame_gui
manager = pygame_gui.UIManager(WINDOW_SIZE)

# Criando uma instância de pygame_gui.TextEntryLine
text_entry_line = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 100), (200, 50)), manager=manager)

# Criando um botão para aumentar o tamanho do texto
increase_font_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 100), (50, 50)), text='+', manager=manager)

# Criando um botão para diminuir o tamanho do texto
decrease_font_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 100), (50, 50)), text='-', manager=manager)

# Definindo o tamanho inicial da fonte
font_size = 20
text_entry_line.font_size = font_size

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Passando eventos para o gerenciador de eventos pygame_gui
        manager.process_events(event)

        # Aumentando o tamanho da fonte ao clicar no botão '+'
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == increase_font_button:
                font_size += 5
                text_entry_line.font_size = font_size

        # Diminuindo o tamanho da fonte ao clicar no botão '-'
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == decrease_font_button:
                font_size -= 5
                text_entry_line.font_size = font_size

    # Atualizando a interface pygame_gui
    manager.update(time_delta)

    # Desenhando na tela
    screen.fill(WHITE)
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()