import pygame

class Score:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.font = pygame.font.SysFont('couriernew', 15)
    
    def draw(self, screen, player):
        text_surface = self.font.render('Score: ' + str(player.score), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.position
        screen.blit(text_surface, text_rect)
