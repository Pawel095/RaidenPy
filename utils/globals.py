import arcade
from utils.loader import Loader


class keyFlags():
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.space = False


WIDTH = 600
HEIGHT = 600
l = Loader()
print("load Start")
l.load()
print("load End")
enemyBullets = arcade.SpriteList()
playerBullets = arcade.SpriteList()
enemies = arcade.SpriteList()
explosions = arcade.SpriteList()


