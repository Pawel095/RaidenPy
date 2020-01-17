import arcade
from game import MenuView

WIDTH = 600
HEIGHT = 600

def main():
    window = arcade.Window(WIDTH, HEIGHT, "DEBUG SHA!^")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()