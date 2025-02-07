import pygame
from settings import WIDTH, HEIGHT


def draw_grid(screen, grid_size):
    """Draw a simple grid for the monastery layout."""
    for x in range(0, WIDTH, grid_size):  # Vertical lines
        pygame.draw.line(screen, (100, 100, 100), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, grid_size):  # Horizontal lines
        pygame.draw.line(screen, (100, 100, 100), (0, y), (WIDTH, y))

    """When cursor hovers over tile, indicate to user."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    highlight_x = (mouse_x // grid_size) * grid_size
    highlight_y = (mouse_y // grid_size) * grid_size

    highlight_rect = pygame.Rect(
        highlight_x, highlight_y, grid_size, grid_size
        )
    pygame.draw.rect(screen, (200, 200, 200), highlight_rect, 2)
