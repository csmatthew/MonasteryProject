import pygame
import math


class Abbot:
    def __init__(self, x, y, grid_size):
        self.grid_size = grid_size
        self.x = (x // grid_size) * grid_size + grid_size // 2
        self.y = (y // grid_size) * grid_size + grid_size // 2
        self.target_x = self.x  # Target position
        self.target_y = self.y
        self.radius = 10
        self.speed = 1  # Movement speed
        self.path = []  # Store the calculated path
        self.health = 100  # Initialize health
        self.score = 0  # Initialize score

    def move_towards_target(self, obstacles):
        """
        Move abbot step by step towards target position, stopping at obstacles.
        """
        next_x, next_y = self.x, self.y

        if self.x < self.target_x:
            next_x += min(self.speed, self.target_x - self.x)
        elif self.x > self.target_x:
            next_x -= min(self.speed, self.x - self.target_x)

        if self.y < self.target_y:
            next_y += min(self.speed, self.target_y - self.y)
        elif self.y > self.target_y:
            next_y -= min(self.speed, self.y - self.target_y)

        # Check for collisions with obstacles
        if not self.check_collision(next_x, next_y, obstacles):
            self.x, self.y = next_x, next_y

        # Remove the points from the path that the abbot has passed over
        if self.path and (self.x, self.y) == self.path[0]:
            self.path.pop(0)

    def check_collision(self, next_x, next_y, obstacles):
        """Check for collisions with obstacles at the next position."""
        abbot_rect = pygame.Rect(
            next_x - self.radius, next_y - self.radius,
            self.radius * 2, self.radius * 2
        )
        for obstacle in obstacles:
            if abbot_rect.colliderect(obstacle.rect):
                return True
        return False

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

        # Calculate the path when the target is set
        self.path = self.calculate_path()

    def draw(self, screen, color):
        """Draw the abbot on the screen."""
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        self.draw_path(screen, color)

    def calculate_path(self):
        """
        Calculate the path from the current position to the target position.
        """
        path = []
        current_x, current_y = self.x, self.y

        while current_x != self.target_x or current_y != self.target_y:
            if current_x < self.target_x:
                current_x += min(self.speed, self.target_x - current_x)
            elif current_x > self.target_x:
                current_x -= min(self.speed, current_x - self.target_x)

            if current_y < self.target_y:
                current_y += min(self.speed, self.target_y - current_y)
            elif current_y > self.target_y:
                current_y -= min(self.speed, current_y - self.target_y)

            path.append((current_x, current_y))

        return path

    def draw_path(self, screen, color):
        """Draw the path as a series of dots."""
        for i, (x, y) in enumerate(self.path):
            if i % 5 == 0:  # Draw every 5th point to create a dotted effect
                pygame.draw.circle(screen, color, (x, y), 2)
