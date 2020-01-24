import arcade
from views.game.bullet import Bullet
from utils.globals import enemyBullets, player
import random
from utils.utilFunctions import getDist, approach, clamp
import math


class Enemy(arcade.Sprite):
    """ ma lecieć do losowego koorda>=200, obracać się w strone gracza i szczelać. bullety tutaj"""

    def __init__(self):
        super().__init__(None)
        self.lastShotTime = 0
        self.shotCooldown = 2

        self.target = [random.randint(300, 500), random.randint(300, 500)]
        self.position = [random.randint(0, 600), 700]

        self.lookDirection = 0
        self.speed = 5
        self.bulletSlow = 100

        self.maxDist = getDist(self.position, self.target)
        self.maxDistX = math.sqrt(
            math.pow(self.position[0]-self.target[0], 2))+1e-3
        self.maxDistY = math.sqrt(
            math.pow(self.position[1]-self.target[1], 2))+1e-3

    def update(self, uptime):
        speedX = 0
        speedY = 0
        if getDist(self.position, self.target) < 70:
            # stój i strzelaj
            if self.lastShotTime+self.shotCooldown < uptime:
                self.lastShotTime = uptime
                pX = (player.position[0]-self.position[0])/self.bulletSlow
                pY = (player.position[1]-self.position[1])/self.bulletSlow
                enemyBullets.append(
                    Bullet(self.position, pX, pY, angle=math.degrees(math.atan(pY/pX))))
        else:
            # leć do target
            wX = self.target[0]-self.position[0]
            wY = self.target[1]-self.position[1]

            speedX = (wX/self.maxDistX)*self.speed
            speedY = (wY/self.maxDistY)*self.speed

        self.change_x = approach(self.change_x, speedX, 0.1)
        self.change_y = approach(self.change_y, speedY, 0.1)
        super().update()

    def draw(self):
        # debugLine
        arcade.draw_line(self.position[0], self.position[1],
                         self.target[0], self.target[1], arcade.color.DARK_BLUE)

        arcade.draw_rectangle_filled(
            self.position[0], self.position[1], 50, 50, arcade.color.DARK_BLUE, self.position[1])
