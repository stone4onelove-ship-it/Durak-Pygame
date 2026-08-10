from game import Game
from brain import think



def main():
    game = Game(passing=False)
    game.init()

    while True:
        game.print_info()
        index = int(input())
        game.play(index)

        think(game.get_user_info(0))
        
        


if __name__ == "__main__":
    main()