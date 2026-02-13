import pygame
from player import Player

class Life(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rotation = 180
        self.radius -= 10

    def update(self):
        pass

