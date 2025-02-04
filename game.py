import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monastery Growth Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with a color (e.g., light brown)
    screen.fill((181, 136, 99))  # RGB color

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
