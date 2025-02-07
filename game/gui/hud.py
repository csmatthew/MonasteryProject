import pygame
from settings import WIDTH, HEIGHT, WHITE


class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.health = 100
        self.score = 0

    def update(self, health, score):
        self.health = health
        self.score = score

    def draw(self, screen):
        health_text = self.font.render(f"Health: {self.health}", True, WHITE)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(health_text, (10, 10))
        screen.blit(score_text, (WIDTH - 150, 10))
