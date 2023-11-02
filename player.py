import pygame
from game_config import *

class Player:
    def __init__(self):
        self.player_pos = pygame.Vector2(game_width / 2, game_height / 2)
        self.player_ms = 300

    def playerMove(self, dt, player_ms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player_pos.y -= player_ms * dt
        if keys[pygame.K_s] or keys [pygame.K_DOWN]:
            self.player_pos.y += player_ms * dt
        if keys[pygame.K_a] or keys [pygame.K_LEFT]:
            self.player_pos.x -= player_ms * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos.x += player_ms * dt 

        if self.player_pos.x >= 1300:
            self.player_pos.x = 0

        if self.player_pos.x <= -20:
            self.player_pos.x = 1280

        if self.player_pos.y >= 740:
            self.player_pos.y = 0
        
        if self.player_pos.y <= -20: 
            self.player_pos.y = 720