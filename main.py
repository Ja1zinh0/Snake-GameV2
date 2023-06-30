import pygame
import random
from pygame.locals import *
from screen import Screen
from snake import Snake
from food import Food

restart = False
def start_game():
    pygame.init()

    screen = Screen()
    snake = Snake()
    apple = Food()
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def random_grid():
        x = random.randint(0, 29)
        y = random.randint(0, 29)
        return (x * 20, y * 20)

    apple_position = random_grid()
    apple = pygame.Surface((20, 20))
    apple.fill((255, 0, 0))

    def restart_game():
        global apple_position
        snake.snake = [(200, 200), (220, 200), (240, 200)]
        snake.direction = RIGHT
        apple_position = random_grid()

    game_on = True
    changing_direction = False
    clock = pygame.time.Clock()
    while game_on:
        clock.tick(18)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            if event.type == KEYDOWN and not changing_direction:
                if event.key == K_UP or event.key == K_w and snake.direction != DOWN:
                    snake.direction = UP
                    changing_direction = True
                if event.key == K_DOWN or event.key == K_s and snake.direction != UP:
                    snake.direction = DOWN
                    changing_direction = True
                if event.key == K_LEFT or event.key == K_a and snake.direction != RIGHT:
                    snake.direction = LEFT
                    changing_direction = True
                if event.key == K_RIGHT or event.key == K_d and snake.direction != LEFT:
                    snake.direction = RIGHT
                    changing_direction = True
                        
        if snake.collision(snake.snake[0], apple_position):
            apple_position = random_grid()
            snake.snake.append((0, 0))
            
        if snake.snake[0][0] == 600 or snake.snake[0][1] == 600 or snake.snake[0][0] < 0 or snake.snake[0][1] < 0:
            game_on = False
            
        for i in range(1, len(snake.snake) - 2):
            if snake.snake[0][0] == snake.snake[i][0] and snake.snake[0][1] == snake.snake[i][1]:
                game_on = False
                break
        
        for i in range(len(snake.snake) - 1, 0, -1):
            snake.snake[i] = (snake.snake[i - 1][0], snake.snake[i - 1][1])
            
        if snake.direction == UP:
            snake.snake[0] = (snake.snake[0][0], snake.snake[0][1] - 20)
        if snake.direction == DOWN:
            snake.snake[0] = (snake.snake[0][0], snake.snake[0][1] + 20)
        if snake.direction == LEFT:
            snake.snake[0] = (snake.snake[0][0] - 20, snake.snake[0][1])
        if snake.direction == RIGHT:
            snake.snake[0] = (snake.snake[0][0] + 20, snake.snake[0][1])
        
        changing_direction = False
         
        screen.window.fill((74, 101, 148))
        screen.blit(apple, apple_position)
        
        for x in range(0, 600, 20):
            pygame.draw.line(screen.window, (40, 40, 40), (x, 0), (x, 600))
            pygame.draw.line(screen.window, (40, 40, 40), (0, x), (600, x))
        
        for position in snake.snake:
            screen.blit(snake.snake_skin, position)
             
        pygame.display.update()

    # Tela de Game Over
    game_over_font = pygame.font.Font('freesansbold.ttf', 60)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 // 2, 10)
    
    additional_text_font = pygame.font.Font('freesansbold.ttf', 30)
    additional_text_screen = additional_text_font.render('Press backspace to play again', True, (255, 255, 255))
    additional_text_rect = additional_text_screen.get_rect()
    additional_text_rect.midtop = (600 // 2, game_over_rect.bottom)
    
    

    screen.window.blit(game_over_screen, game_over_rect)
    screen.window.blit(additional_text_screen, additional_text_rect)
    pygame.display.update()

    while game_on == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    restart_game()
                    start_game()

start_game()
