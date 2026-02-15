import pygame
from constants import LINE_WIDTH

class LifeIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.rotation = 180
        self.radius = 10
        self.position = pygame.Vector2(x, y)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

