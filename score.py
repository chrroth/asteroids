import pygame
from player import Player

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen, player):
        score_font = pygame.font.SysFont('couriernew', 15)
        score = player.score
        #score = 10
        text_surface = score_font.render('Score: ' + str(score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.position
        screen.blit(text_surface, text_rect)
