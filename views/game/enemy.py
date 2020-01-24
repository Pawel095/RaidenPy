import arcade
from views.game.bullet import Bullet
# from utils.globals import bullets
import utils.globals
import random
from utils.utilFunctions import getDist, approach, clamp
import math


class Enemy(arcade.Sprite):
    """ ma lecieć do losowego koorda>=200, obracać się w strone gracza i szczelać. bullety tutaj"""

    def __init__(self):
        super().__init__(None)
        # bullets.append(Bullet([200, 200], 0, 1, color=arcade.color.JAPANESE_INDIGO))
        print("spawning enemy")
        self.lastShotTime = -9999
        self.shotCooldown = 2
        self.target = [random.randint(100, 500), random.randint(100, 500)]
        self.lookDirection = 0
        self.position = [100, 100]
        self.speed = 5
        self.maxDist = getDist(self.position, self.target)

    def update(self, uptime):
        if getDist(self.position, self.target) < 100:
            if uptime+self.shotCooldown < self.lastShotTime:
                self.lastShotTime = uptime
                print("SHOT!")
        else:
            # leć do target
            # approach(self.position[0], self.target[0], 0.1)
            wX = math.sqrt(math.pow(self.position[0]-self.target[0], 2))
            wY = math.sqrt(math.pow(self.position[1]-self.target[1], 2))

            # self.change_x = deltaX
            # self.change_y = deltaY
            super().update()
            pass

    def draw(self):
        arcade.draw_rectangle_filled(
            self.position[0], self.position[1], 50, 50, arcade.color.DARK_BLUE, self.position[1])
