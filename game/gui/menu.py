import pygame
import pygame_gui
from settings import WIDTH, HEIGHT


class Menu:
    def __init__(self, manager):
        self.manager = manager
        self.main_menu = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(
                (WIDTH // 4, HEIGHT // 4),
                (WIDTH // 2, HEIGHT // 2)
                ),
            manager=self.manager,
            window_display_title="Main Menu",
            object_id="#main_menu"
        )
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 50), (200, 50)),
            text='Start Game',
            manager=self.manager,
            container=self.main_menu
        )
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((50, 150), (200, 50)),
            text='Quit',
            manager=self.manager,
            container=self.main_menu
        )

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    print("Start Game button pressed")
                    self.main_menu.hide()  # Hide the main menu
                    # Add logic to start the game
                elif event.ui_element == self.quit_button:
                    print("Quit button pressed")
                    pygame.quit()
                    exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.main_menu.visible:
                    self.main_menu.hide()
                else:
                    self.main_menu.show()

    def draw(self, screen):
        self.manager.draw_ui(screen)
