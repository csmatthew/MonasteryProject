import pygame
import pygame_gui
from settings import WIDTH, HEIGHT


class MapView:
    def __init__(self, manager):
        self.manager = manager
        self.map_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(
                (WIDTH // 4, HEIGHT // 4),
                (WIDTH // 2, HEIGHT // 2)
                ),
            manager=self.manager,
            window_display_title="Map View",
            object_id="#map_view"
        )
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 50), (200, 50)),
            text='Back to Menu',
            manager=self.manager,
            container=self.map_window
        )

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.back_button:
                    print("Back to Menu button pressed")
                    self.map_window.hide()  # Hide the map view
                    return 'menu'  # Return to the menu view

    def draw(self, screen):
        self.manager.draw_ui(screen)