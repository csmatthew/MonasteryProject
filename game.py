import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monastery Growth Game")

# Colors
LIGHT_BROWN = (181, 136, 99)  # Background color
WHITE = (255, 255, 255)        # Abbot color (white dot)

# Set abbot's starting position
abbot_x, abbot_y = WIDTH // 2, HEIGHT // 2
ABBOT_RADIUS = 10  # Size of the dot

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(LIGHT_BROWN)

    # Draw the abbot as a circle
    pygame.draw.circle(screen, WHITE, (abbot_x, abbot_y), ABBOT_RADIUS)

    # Refresh screen
    pygame.display.update()

pygame.quit()