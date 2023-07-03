import pygame
import asyncio
from pygame.locals import *
from screen import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import sys

def start_game():
    pygame.init()
    
    #creating objects
    screen = Screen()
    snake = Snake()
    apple = Food()
    scoreboard = Scoreboard()

    apple_position = apple.generate_position()
    game_on = True
    changing_direction = False
    clock = pygame.time.Clock()
    
    while game_on:
        #controlling game speed
        clock.tick(18)
                
        #checking collisions
        if snake.apple_collision(snake.snake[0], apple_position):
            apple_position = apple.generate_position()
            snake.snake.append((0, 0))
            scoreboard.increase_score()
            
        if snake.wall_collision():
            game_on = False
            
        if snake.self_collision():
            game_on = False
                
        #controlling the snake movement
        snake.control_movement(changing_direction)
        
        #refreshing the screen to create a new apple and remove the snake trail
        screen.refresh(apple.apple_skin, apple_position)
        
        #drawing the game grid
        screen.draw_grid()
        
        #drawing the snake
        for position in snake.snake:
            screen.blit(snake.snake_skin, position)
            
        #creating the scoreboard
        screen.window.blit(scoreboard.score_screen, scoreboard.score_rect)
        
        #reseting the snake direction
        changing_direction = False
        
        #updating the screen
        pygame.display.update()
        
    #show the game over screen
    screen.game_over(scoreboard.score)
    
    #restart or quit the game
    while not game_on:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    start_game()
    
start_game()