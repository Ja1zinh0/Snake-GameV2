import pygame
pygame.init()

class Scoreboard():
    def __init__(self):
        self.score = 0
        self.score_font = pygame.font.Font('freesansbold.ttf', 20)
        self.score_screen = self.score_font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.score_rect = self.score_screen.get_rect(topleft=(5,5))
        
    def update_score_screen(self):
        self.score_screen = self.score_font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.score_rect = self.score_screen.get_rect(topleft=(5,5))
        
    def increase_score(self):
        self.score += 1
        self.update_score_screen()
        
        