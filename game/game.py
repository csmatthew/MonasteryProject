import pygame
import pygame_gui
from settings import WIDTH, HEIGHT, FPS, LIGHT_BROWN, WHITE
from entities.abbot import Abbot
from entities.obstacle import Obstacle
from entities.npc import NPC
from gui.grid import draw_grid
from gui.hud import HUD
# from gui.menu import Menu
# from gui.map_view import MapView

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

# Create an instance of NPC
npc = NPC(150, 150, grid_size, WIDTH, HEIGHT)

# Initialize pygame_gui
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Create HUD, Menu, and MapView
hud = HUD()
# menu = Menu(manager)
# map_view = MapView(manager)

# Set initial view
current_view = 'game'  # Start directly in game view
previous_view = None
game_paused = False


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
    time_delta = clock.tick(FPS) / 1000.0  # Time in seconds since last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle events based on the current view
        # if current_view == 'menu':
        #     view_result = menu.handle_events(event)
        #     if view_result:
        #         current_view = view_result
        #         game_paused = current_view == 'menu'
        # elif current_view == 'map':
        #     view_result = map_view.handle_events(event)
        #     if view_result:
        #         current_view = view_result
        # elif current_view == 'game':
        if current_view == 'game':
            if event.type == pygame.MOUSEBUTTONDOWN and not game_paused:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                abbot.set_target(mouse_x, mouse_y, WIDTH, HEIGHT)
            # elif (event.type == pygame.KEYDOWN and
            #       event.key == pygame.K_ESCAPE):
            #     if menu.main_menu.visible:
            #         menu.main_menu.hide()
            #         game_paused = False
            #     else:
            #         menu.main_menu.show()
            #         game_paused = True

        # Pass events to pygame_gui
        manager.process_events(event)

    # Update pygame_gui
    manager.update(time_delta)

    # Update game state based on the current view
    if current_view == 'game' and not game_paused:
        abbot.move_towards_target(obstacles)
        npc.move(obstacles)

    # Draw based on the current view
    screen.fill(LIGHT_BROWN)
    # if current_view == 'menu':
    #     draw_grid(screen, grid_size)
    #     abbot.draw(screen, WHITE)
    #     for obstacle in obstacles:
    #         obstacle.draw(screen, (0, 0, 0))  # Draw obstacles in black
    #     hud.draw(screen)
    #     menu.draw(screen)
    # elif current_view == 'map':
    #     map_view.draw(screen)
    if current_view == 'game':
        draw_grid(screen, grid_size)
        abbot.draw(screen, WHITE)
        npc.draw(screen)  # <-- Draw the NPC
        for obstacle in obstacles:
            obstacle.draw(screen, (0, 0, 0))  # Draw obstacles in black
        hud.draw(screen)
        # if menu.main_menu.visible:
        #     menu.draw(screen)

    # Refresh screen
    pygame.display.update()

pygame.quit()
