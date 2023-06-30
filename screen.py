import pygame
BACKGROUND = (74, 101, 148)
pygame.init()

class Screen():
    def __init__(self):
        window_width = 600
        window_lengh = 600
        self.window = pygame.display.set_mode((window_width, window_lengh))
        self.window.fill(BACKGROUND)
        pygame.display.set_caption("Snake")
    
    def blit(self, surface, position):
        self.window.blit(surface, position)