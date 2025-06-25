import random
import pygame
import math


class NPC:
    def __init__(
        self, x, y, grid_size, screen_width, screen_height, color=(0, 100, 255)
    ):
        self.grid_size = grid_size
        self.radius = 10
        self.speed = 1
        self.x = (x // grid_size) * grid_size + grid_size // 2
        self.y = (y // grid_size) * grid_size + grid_size // 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = color
        self.target_x, self.target_y = self.get_random_target()

    def get_random_target(self):
        max_x = (self.screen_width - self.radius) // self.grid_size
        max_y = (self.screen_height - self.radius) // self.grid_size
        rand_x = (random.randint(0, max_x) * self.grid_size +
                  self.grid_size // 2)
        rand_y = (random.randint(0, max_y) * self.grid_size +
                  self.grid_size // 2)
        return rand_x, rand_y

    def move(self, obstacles):
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.hypot(dx, dy)

        next_x, next_y = self.x, self.y

        if distance != 0:
            dx = dx / distance * self.speed
            dy = dy / distance * self.speed
            next_x = self.x + int(round(dx))
            next_y = self.y + int(round(dy))

        # Optional: collision check here
        self.x, self.y = next_x, next_y

        if self.x == self.target_x and self.y == self.target_y:
            self.target_x, self.target_y = self.get_random_target()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
