import pygame
from pygame.locals import *
pygame.init()

SNAKE_COLOR = (214, 215, 255)
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Snake():
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.snake_skin = pygame.Surface((20,20))
        self.snake_skin.fill(SNAKE_COLOR)
        self.direction = ""
      
    def apple_collision(self, c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])
    
                    
    def wall_collision(self):
        if self.snake[0][0] == 600 or self.snake[0][1] == 600 or self.snake[0][0] < 0 or self.snake[0][1] < 0:
            return True
    
    def self_collision(self):
        for i in range(1, len(self.snake) - 2):
            if self.snake[0][0] == self.snake[i][0] and self.snake[0][1] == self.snake[i][1]:
                return True
            
    def control_movement(self, changing_direction):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i - 1][0], self.snake[i - 1][1])
            
        for event in pygame.event.get():
            if event.type == KEYDOWN and not changing_direction:
                if event.key == K_UP or event.key == K_w and self.direction != DOWN:
                    self.direction = UP
                    changing_direction = True
                if event.key == K_DOWN or event.key == K_s and self.direction != UP:
                    self.direction = DOWN
                    changing_direction = True
                if event.key == K_LEFT or event.key == K_a and self.direction != RIGHT:
                    self.direction = LEFT
                    changing_direction = True
                if event.key == K_RIGHT or event.key == K_d and self.direction != LEFT:
                    self.direction = RIGHT
                    changing_direction = True
         
        if self.direction == UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - 20)
        if self.direction == DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + 20)
        if self.direction == LEFT:
            self.snake[0] = (self.snake[0][0] - 20, self.snake[0][1])
        if self.direction == RIGHT:
            self.snake[0] = (self.snake[0][0] + 20, self.snake[0][1])