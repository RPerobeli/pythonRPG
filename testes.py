import pygame
import time

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the screen
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set the font and font size
font = pygame.font.Font(None, 32)

# Define the text to be displayed
text = "Hello, this is a dialog box with typewriter effect."

# Define the position of the dialog box
x = 50
y = 50

# Define the delay time between each character display
delay = 50

# Loop until the user clicks the close button
done = False
clock = pygame.time.Clock()

# Function to display text with typewriter effect
def text_effect(text, x, y, delay):
    # Loop through each character in the text
    for i in range(len(text)):
        # Render the text up to the current character
        rendered_text = font.render(text[:i+1], True, BLACK)
        # Get the dimensions of the rendered text
        text_rect = rendered_text.get_rect()
        # Set the position of the text
        text_rect.x = x
        text_rect.y = y
        # Blit the text to the screen
        screen.blit(rendered_text, text_rect)
        pygame.display.flip()
        # Wait for a short time before displaying the next character
        time.sleep(delay / 1000)

        # Check if the user has pressed the spacebar
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Display the rest of the text and return
                    rendered_text = font.render(text[i+1:], True, BLACK)
                    text_rect = rendered_text.get_rect()
                    text_rect.x = x + text_rect.width
                    text_rect.y = y
                    screen.blit(rendered_text, text_rect)
                    pygame.display.flip()
                    return

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Fill the background with white
    screen.fill(WHITE)
    
    # Display the text with typewriter effect
    text_effect(text, x, y, delay)
    
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()
