import pygame

class Abbot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.speed = 2

    def move(self, keys, width, height):
        """Move the abbot based on key inputs."""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

        # Keep within screen bounds
        self.x = max(self.radius, min(width - self.radius, self.x))
        self.y = max(self.radius, min(height - self.radius, self.y))

    def draw(self, screen, color):
        """Draw the abbot on the screen."""
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
