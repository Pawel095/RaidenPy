import arcade
from views.game.bullet import Bullet
from utils.flags import bullets
import random
from utils.utilFunctions import getDist


class Enemy(arcade.Sprite):
    """ ma lecieć do losowego koorda>=200, obracać się w strone gracza i szczelać. bullety tutaj"""

    def __init__(self):
        # bullets.append(Bullet([200,200],0,1,color=arcade.color.JAPANESE_INDIGO))
        self.lastShotTime = -9999
        self.shotCooldown = 2
        self.target = [random.randint(100, 500), random.randint(100, 500)]

    def update(self, uptime):
        if getDist(self.position, self.target)<100:
            if uptime+self.shotCooldown < self.lastShotTime:
                self.lastShotTime = uptime
                print("SHOT!")
        else:
            pass


def draw(self):
    pass
