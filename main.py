import arcade
from views.game.game import GameView
from utils.globals import WIDTH, HEIGHT
import utils.globals
import utils.views
from utils.loader import Loader


def main():
    utils.globals.WINDOW = arcade.Window(
        utils.globals.WIDTH, utils.globals.HEIGHT, utils.globals.TITLE
    )
    l = Loader()
    l.load()

    utils.globals.WINDOW.show_view(utils.views.game_view)
    arcade.run()


if __name__ == "__main__":
    main()
