import random
import pygame
pygame.init()

class Food:
    def __init__(self):
        self.x = random.randint(0,29)
        self.y = random.randint(0,29)

    