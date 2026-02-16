import pygame
from utils import get_triangle_vertices
from constants import LINE_WIDTH

class LifeIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.rotation = 180
        self.radius = 10
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        vertices = get_triangle_vertices(self.position, self.rotation, self.radius)
        pygame.draw.polygon(screen, "white", vertices, LINE_WIDTH)

