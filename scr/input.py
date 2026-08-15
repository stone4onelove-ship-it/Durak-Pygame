import pygame
from game import Game
from game.brain import Brain



def handle_input(game: Game) -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False

        if event.type == pygame.KEYDOWN:
            if pygame.K_0 <= event.key <= pygame.K_9:
                index = event.key - pygame.K_0  # converts key to actual int
                game.play(index)
                game.brain.think(game.viewpoint(0))
                print(game.brain)
                print(game)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.play(-1)
                game.brain.think(game.viewpoint(0))
                print(game.brain)
                print(game)

    return True