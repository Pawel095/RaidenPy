import arcade
from views.game.bullet import Bullet
from utils.globals import enemyBullets, player
from utils.loader import assets
import random
from utils.utilFunctions import getDist, approach, clamp
import math


class Enemy(arcade.Sprite):
    """ ma lecieć do losowego koorda>=200, obracać się w strone gracza i szczelać. bullety tutaj"""

    def __init__(self,scale=1):
        super().__init__(None)
        self._texture = assets["enemy1"]
        if self._texture:
            self.textures = [self._texture]
            self._width = self._texture.width*scale
            self._height = self._texture.height*scale
            self._texture.scale = scale
        self.lastShotTime = 0
        self.shotCooldown = 2

        # self.target = [random.randint(100, 500), random.randint(100, 500)]
        # self.position = [random.randint(0, 600), 500]
        self.target = [300,300]
        self.position = [300,300]

        self.lookDirection = 0
        self.speed = 5
        self.bulletSlow = 100
        self.maxDistX = math.sqrt(
            math.pow(self.position[0]-self.target[0], 2))+1e-3
        self.maxDistY = math.sqrt(
            math.pow(self.position[1]-self.target[1], 2))+1e-3

    def update(self, uptime):
        speedX = 0
        speedY = 0
        targetAngle=180
        if getDist(self.position, self.target) < 70:
            # stój i strzelaj,obracając się w sron gracza
            pX = (player.position[0]-self.position[0])/self.bulletSlow
            pY = (player.position[1]-self.position[1])/self.bulletSlow
            targetAngle = math.degrees(math.atan2(pY,pX))-90
            if self.lastShotTime+self.shotCooldown < uptime:
                self.lastShotTime = uptime
                enemyBullets.append(
                    Bullet(self.position, pX, pY, angle=targetAngle))
        else:
            # leć do target
            wX = self.target[0]-self.position[0]
            wY = self.target[1]-self.position[1]

            targetAngle = math.degrees(math.atan2(wY,wX))

            speedX = (wX/self.maxDistX)*self.speed
            speedY = (wY/self.maxDistY)*self.speed

        self.change_x = approach(self.change_x, speedX, 0.1)
        self.change_y = approach(self.change_y, speedY, 0.1)
        self.angle = approach(self.angle,targetAngle,0.1)
        print(targetAngle)
        super().update()

    def draw(self):
        # debugLine
        # arcade.draw_line(self.position[0], self.position[1],
        #                  self.target[0], self.target[1], arcade.color.DARK_BLUE)
        super().draw()
