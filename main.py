import arcade
import utils.globals
from utils.loader import Loader
import utils.views




WIDTH = 600
HEIGHT = 600



def main():
    utils.globals.WINDOW = arcade.Window(utils.globals.SCREEN_WIDTH, utils.globals.SCREEN_HEIGHT, utils.globals.SCREEN_TITLE)
    l = Loader()
    l.load()
    
    utils.globals.WINDOW.show_view(utils.views.main_menu)
    arcade.run()


if __name__ == "__main__":
    main()