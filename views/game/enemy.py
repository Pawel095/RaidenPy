import arcade
from views.game.bullet import Bullet
from views.game.explosion import Explosion
from utils.globals import enemyBullets, player, explosions
from utils.loader import assets
import random
from utils.utilFunctions import getDist, approach, clamp
import math


class Enemy(arcade.Sprite):
    """ ma lecieć do losowego koorda>=200, obracać się w strone gracza i szczelać. bullety spawnowane tutaj"""

    def __init__(self, scale=1):
        super().__init__(None)
        self._texture = assets["enemy1"]
        if self._texture:
            self.textures = [self._texture]
            self._width = self._texture.width*scale
            self._height = self._texture.height*scale
            self._texture.scale = scale

        self.hp = 2

        self.lastShotTime = 0
        self.shotCooldown = 2

        self.lastBlinkTriggerTime = 0
        self.blinkTime = 0.5
        self.blinkStatus = False
        self._blinker = 0

        self.target = [random.randint(100, 500), random.randint(100, 500)]
        self.position = [random.randint(0, 600), 700]
        # self.target = [300,300]
        # self.position = [300,300]

        self.lookDirection = 0
        self.speed = 5
        self.bulletSpeed = 5
        self.maxDistX = math.sqrt(
            math.pow(self.position[0]-self.target[0], 2))+1e-3
        self.maxDistY = math.sqrt(
            math.pow(self.position[1]-self.target[1], 2))+1e-3

    def update(self, uptime):
        speedX = 0
        speedY = 0
        targetAngle = 180
        if getDist(self.position, self.target) < 70:
            # stój i strzelaj,obracając się w sron gracza

            pX = (player.position[0]-self.position[0])
            pY = (player.position[1]-self.position[1])
            pAngle = math.atan2(pY, pX)
            targetAngle = math.degrees(pAngle)-90
            if self.lastShotTime+self.shotCooldown < uptime:
                self.lastShotTime = uptime
                bX = math.cos(pAngle)
                bY = math.sin(pAngle)

                enemyBullets.append(
                    Bullet(self.position, bX*self.speed, bY*self.speed, angle=math.degrees(pAngle)-90, color="r"))
        else:
            # leć do target
            wX = self.target[0]-self.position[0]
            wY = self.target[1]-self.position[1]

            targetAngle = math.degrees(math.atan2(wY, wX))-90

            speedX = (wX/self.maxDistX)*self.speed
            speedY = (wY/self.maxDistY)*self.speed

        self.change_x = approach(self.change_x, speedX, 0.1)
        self.change_y = approach(self.change_y, speedY, 0.1)
        self.angle = approach(self.angle, targetAngle, 0.1)

        if self.blinkTime+self.lastBlinkTriggerTime < uptime:
            self.blinkStatus = False
            self._blinker = 0

        if self.hp <= 0:
            self.kill()

        super().update()

    def onHit(self, uptime):
        if not self.blinkStatus:
            self.blinkStatus = True
            self.lastBlinkTriggerTime = uptime
            self.hp -= 1

    def kill(self):
        explosions.append(Explosion(self.position,scale=3))
        super().kill()

    def draw(self):
        if self.blinkStatus:
            self._blinker += 1
            if self._blinker % 3 == 0:
                super().draw()
        else:
            super().draw()
