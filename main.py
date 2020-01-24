import arcade
from views.game.game import GameView
from utils.loader import Loader

WIDTH = 600
HEIGHT = 600

def main():
    window = arcade.Window(WIDTH, HEIGHT, "DEBUG SHA!^")
    l = Loader()
    print("load Start")
    l.load()
    print("load End")
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()