import pygame
pygame.init()

BACKGROUND = (74, 101, 148)

class Screen():
    def __init__(self):
        window_width = 600
        window_lengh = 600
        self.window = pygame.display.set_mode((window_width, window_lengh))
        self.window.fill(BACKGROUND)
        pygame.display.set_caption("Snake")
    
    def blit(self, surface, position):
        self.window.blit(surface, position)
        
    def refresh(self, apple, apple_position):
        self.window.fill((74, 101, 148))
        self.window.blit(apple, apple_position)
        
    def draw_grid(self):
        for x in range(0, 600, 20):
            pygame.draw.line(self.window, (40, 40, 40), (x, 0), (x, 600))
            pygame.draw.line(self.window, (40, 40, 40), (0, x), (600, x))
            
    def render_text(self, text, font_name, font_size, color, x, y):
        font = pygame.font.SysFont(font_name, font_size)
        text_surface = font.render(text, True, color)
        self.text_rect = text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        self.window.blit(text_surface, self.text_rect)

    def game_over(self, score):
        final_screen = Screen()
        self.render_text('Game Over', 'courier', 60, (255, 255, 255), 600 // 2, 10)
        self.render_text('Press R to play again', 'courier', 30, (255, 255, 255), 600 // 2, self.text_rect.bottom)
        self.render_text(f'Final score: {score}', 'courier', 30, (255, 255, 255), 600 // 2, self.text_rect.bottom)
        pygame.display.update()
        