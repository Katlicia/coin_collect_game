import pygame
import random
import math
from game_config import *

class Coin:

    def __init__(self):
        self.coin_pos = pygame.Vector2(random.randint(10, game_width - 40), random.randint(10, game_height - 40))
        self.radius = 20
        self.coin_time = 2000
        self.coin_spawn_time = pygame.time.get_ticks() + self.coin_time

    def check_collision(self, player_pos):
        distance = math.sqrt((self.coin_pos.x - player_pos.x) ** 2 + (self.coin_pos.y - player_pos.y) ** 2)
        if distance < self.radius + 40:
            return True
        return False