import pygame
from screen import Screen
pygame.init()

SNAKE_COLOR = (214, 215, 255)
BORDER_COLOR = (0,0,0)

class Snake():
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.snake_skin = pygame.Surface((20,20))
        self.snake_skin.fill(SNAKE_COLOR)
        self.direction = "right"
      
    def collision(self, c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])
    
        