import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_value = random.uniform(20, 50)
            new_velocity_01 = self.velocity.rotate(random_value)
            new_velocity_02 = self.velocity.rotate(-random_value)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_01 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_02 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_01.velocity = new_velocity_01 * 1.2
            asteroid_02.velocity = new_velocity_02 * 1.2