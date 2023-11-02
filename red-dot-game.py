import pygame
from player import Player
from scoreboard import ScoreBoard
from coin import Coin
from game_config import *

# Initializing pygame.

pygame.init()

# Setting up game settings.
pygame.display.set_caption("Red Circle")
screen = pygame.display.set_mode((game_width, game_height))

clock = pygame.time.Clock()

player = Player()
coin = Coin()
score = ScoreBoard()

while running:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background    
    screen.fill("turquoise")

    # Player object features.
    pygame.draw.circle(screen, "red", player.player_pos, 40)
    player.playerMove(dt, player.player_ms)
    
    current_time = pygame.time.get_ticks()

    # Spawning coin.
    if current_time >= coin.coin_spawn_time:
        coin = Coin()

    # Checking collision between coin and player.
    if coin.check_collision(player.player_pos) == True:
        coin = Coin()
        score.score += 1
        coin.coin_spawn_time = current_time + coin.coin_time
        
    pygame.draw.circle(screen, "yellow", coin.coin_pos, 20)

    score.showScore()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()