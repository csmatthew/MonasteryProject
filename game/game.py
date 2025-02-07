import pygame
from settings import WIDTH, HEIGHT, FPS, LIGHT_BROWN, WHITE
from entities.abbot import Abbot
from entities.obstacle import Obstacle
from gui.grid import draw_grid

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

# Create obstacles
obstacles = [
    Obstacle(100, 100, grid_size, grid_size),
    Obstacle(200, 200, grid_size, grid_size),
    Obstacle(300, 300, grid_size, grid_size)
]


def check_collisions(abbot, obstacles):
    """Check for collisions between the abbot and obstacles."""
    abbot_rect = pygame.Rect(
        abbot.x - abbot.radius, abbot.y - abbot.radius,
        abbot.radius * 2, abbot.radius * 2
    )
    for obstacle in obstacles:
        if abbot_rect.colliderect(obstacle.rect):
            return True
    return False


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
    abbot.move_towards_target(obstacles)

    # Draw everything
    screen.fill(LIGHT_BROWN)
    draw_grid(screen, grid_size)
    abbot.draw(screen, WHITE)
    for obstacle in obstacles:
        obstacle.draw(screen, (0, 0, 0))  # Draw obstacles in black

    # Refresh screen
    pygame.display.update()
    clock.tick(FPS)  # Use FPS from settings

pygame.quit()
