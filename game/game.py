import pygame
from settings import WIDTH, HEIGHT, FPS, LIGHT_BROWN, WHITE
from entities.abbot import Abbot

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monastery Growth Game")

# Set up clock
clock = pygame.time.Clock()

# Create an instance of Abbot
abbot = Abbot(WIDTH // 2, HEIGHT // 2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    abbot.move(keys, WIDTH, HEIGHT)

    # Draw everything
    screen.fill(LIGHT_BROWN)
    abbot.draw(screen, WHITE)

    # Refresh screen
    pygame.display.update()
    clock.tick(FPS)  # Use FPS from settings

pygame.quit()
