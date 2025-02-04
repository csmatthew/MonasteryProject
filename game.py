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
ABBOT_SPEED = 2    # Reduced speed for smoother movement

# Set up clock to control frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Movement controls (Arrow keys or WASD)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        abbot_x -= ABBOT_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        abbot_x += ABBOT_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        abbot_y -= ABBOT_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        abbot_y += ABBOT_SPEED

# Keep abbot within screen boundaries
    abbot_x = max(ABBOT_RADIUS, min(WIDTH - ABBOT_RADIUS, abbot_x))
    abbot_y = max(ABBOT_RADIUS, min(HEIGHT - ABBOT_RADIUS, abbot_y))

    # Fill background
    screen.fill(LIGHT_BROWN)

    # Draw the abbot as a circle
    pygame.draw.circle(screen, WHITE, (abbot_x, abbot_y), ABBOT_RADIUS)

    # Refresh screen
    pygame.display.update()

    # Control frame rate (reduces CPU usage and smooths movement)
    clock.tick(60)  # Limits FPS to 60

pygame.quit()
