import pygame
from settings import WIDTH, HEIGHT, FPS, LIGHT_BROWN, WHITE
from entities.abbot import Abbot

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monastery Growth Game")

# Set up clock
clock = pygame.time.Clock()

# Define grid size
grid_size = 20

# Create an instance of Abbot
abbot = Abbot(WIDTH // 2, HEIGHT // 2, grid_size)


def draw_grid(screen):
    """Draw a simple grid for the monastery layout."""
    for x in range(0, WIDTH, grid_size):  # Vertical lines
        pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, grid_size):  # Horizontal lines
        pygame.draw.line(screen, (100, 100, 100), (0, y), (WIDTH, y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            abbot.set_target(mouse_x, mouse_y, WIDTH, HEIGHT)

    # Move abbot towards the target
    abbot.move_towards_target()

    # Draw everything
    screen.fill(LIGHT_BROWN)
    draw_grid(screen)
    abbot.draw(screen, WHITE)

    # Refresh screen
    pygame.display.update()
    clock.tick(FPS)  # Use FPS from settings

pygame.quit()
