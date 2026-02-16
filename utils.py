import pygame

def get_triangle_vertices(position, rotation, radius):
    forward = pygame.Vector2(0, 1).rotate(rotation)
    right = pygame.Vector2(0, 1).rotate(rotation + 90)
    a = position + forward * radius
    b = position - forward * radius - right * radius / 1.5
    c = position - forward * radius + right * radius / 1.5
    return [a, b ,c]
