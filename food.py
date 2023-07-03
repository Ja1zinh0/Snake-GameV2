import random
import pygame
pygame.init()

class Food:
    def __init__(self):
        self.y =0
        self.x = 0
        self.apple_skin = pygame.Surface((20, 20))
        self.apple_skin.fill((255, 0, 0))
        
    def generate_position(self):
        self.x = random.randint(0, 29)
        self.y = random.randint(0, 29)
        return (self.x * 20, self.y * 20)