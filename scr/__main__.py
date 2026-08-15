import pygame
from game import Game
from ui import Ui
from input import handle_input


pygame.init()
clock = pygame.time.Clock()


def main():
    game = Game()
    ui = Ui(game)

    running = True
    while running:
        
        running = handle_input(game)
        ui.update()

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

        
        
if __name__ == "__main__":
    main()