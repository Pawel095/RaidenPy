import arcade
from utils.loader import Loader


class keyFlags():
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.space = False


TITLE = "Raiden Py"
WINDOW = None


WIDTH = 600
HEIGHT = 600
SCREEN_WIDTH = WIDTH
SCREEN_HEIGHT = HEIGHT
bullets = []
enemies = []
l = Loader()
print("load Start")
l.load()
print("load End")
enemyBullets = arcade.SpriteList()
playerBullets = arcade.SpriteList()
enemies = arcade.SpriteList()
explosions = arcade.SpriteList()
