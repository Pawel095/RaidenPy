import arcade
from views.game.game import GameView
from utils.globals import WIDTH,HEIGHT



def main():
    window = arcade.Window(WIDTH, HEIGHT, "DEBUG SHA!^")

    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


if __name__ == "__main__":
    main()