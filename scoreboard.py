import pygame
pygame.init()

class Scoreboard():
    def __init__(self):
        self.score, self.score_font, self.score_screen, self.score_rect = 0, pygame.font.SysFont('courier', 25), None, None
        self.update_score()

    def update_score(self):
        self.score_screen = self.score_font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.score_rect = self.score_screen.get_rect(topleft=(5, 5))
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        
        