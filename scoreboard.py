import pygame

screen = pygame.display.set_mode((1280, 720))

class ScoreBoard:

    def __init__(self):
        self.font = pygame.font.Font("pixel_font.ttf", 36)
        self.score = 0
    
    def showScore(self):
        score_text = self.font.render("Score: " + str(self.score), True, ("Black"))
        screen.blit(score_text, (10, 10))
