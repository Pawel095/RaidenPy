from views.game.player import Player
import arcade


class keyFlags():
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.space = False


WIDTH = 600
HEIGHT = 600
enemyBullets = arcade.SpriteList()
playerBullets = arcade.SpriteList()
enemies = arcade.SpriteList()
player = Player()
