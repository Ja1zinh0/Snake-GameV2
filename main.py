import pygame
import asyncio
from pygame.locals import *
from screen import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def game_loop():
    pygame.init()
    screen = Screen()
    snake = Snake()
    apple = Food()
    scoreboard = Scoreboard()

    apple_position = apple.generate_position()
    game_on = True
    changing_direction = False
    clock = pygame.time.Clock()

    while game_on:
        # Controlling game speed
        clock.tick(18)

        # Checking collisions
        if snake.apple_collision(snake.snake[0], apple_position):
            apple_position = apple.generate_position()
            snake.snake.append((0, 0))
            scoreboard.increase_score()

        if snake.wall_collision():
            game_on = False

        if snake.self_collision():
            game_on = False

        # Controlling the snake movement
        snake.control_movement(changing_direction)

        # Refreshing the screen to create a new apple and remove the snake trail
        screen.refresh(apple.apple_skin, apple_position)

        # Drawing the game grid
        screen.draw_grid()

        # Drawing the snake
        for position in snake.snake:
            screen.blit(snake.snake_skin, position)

        # Creating the scoreboard
        screen.window.blit(scoreboard.score_screen, scoreboard.score_rect)

        # Reseting the snake direction
        changing_direction = False
        
        #saving the final score
        global final_score 
        final_score = scoreboard.score
        
        # Updating the screen
        pygame.display.update()
        
    return game_on


def start_game():
    while True:
        game_on = True
        while game_on:
            game_on = game_loop()

        # Show the game over screen
        screen = Screen()
        screen.game_over(final_score)
        pygame.display.update()

        # Restart or quit the game
        restart = False
        while not restart:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart = True

        pygame.quit()

asyncio.run(start_game())