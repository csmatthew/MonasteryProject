import pygame


class Abbot:
    def __init__(self, x, y, grid_size):
        self.x = x
        self.y = y
        self.grid_size = grid_size
        self.target_x = x  # Target position
        self.target_y = y
        self.radius = 10
        self.speed = 5  # Movement speed

    def move_towards_target(self):
        """Move abbot step by step towards target position."""
        if self.x < self.target_x:
            self.x += min(self.speed, self.target_x - self.x)
        elif self.x > self.target_x:
            self.x -= min(self.speed, self.x - self.target_x)

        if self.y < self.target_y:
            self.y += min(self.speed, self.target_y - self.y)
        elif self.y > self.target_y:
            self.y -= min(self.speed, self.y - self.target_y)

    def set_target(self, mouse_x, mouse_y, width, height):
        """Convert mouse click to nearest grid position
        and keep within screen bounds."""
        self.target_x = (
            mouse_x // self.grid_size
            ) * self.grid_size + self.grid_size // 2
        self.target_y = (
            mouse_y // self.grid_size
            ) * self.grid_size + self.grid_size // 2

        # Keep within screen bounds
        self.target_x = max(
            self.radius, min(
                width - self.radius, self.target_x
            ))
        self.target_y = max(
            self.radius, min(
                height - self.radius, self.target_y
            ))

    def draw(self, screen, color):
        """Draw the abbot on the screen."""
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
