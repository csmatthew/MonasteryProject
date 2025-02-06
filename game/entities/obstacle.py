import pygame


class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
