import arcade
from views.game.bullet import Bullet
from views.game.explosion import Explosion
from utils.globals import enemyBullets, explosions
from utils.loader import assets
import random
from utils.utilFunctions import getDist, approach, clamp
from utils.menusFunctions import getCurrDiff
import math
from utils.menusFunctions import getSoundState


class Enemy(arcade.Sprite):
    """ ma lecieć do losowego koorda>=100, obracać się w strone gracza i szczelać. bullety spawnowane tutaj"""

    def __init__(self, player, scale=1):
        super().__init__(None)
        self.texture = assets["enemy"+str(random.randint(1,3))]
        self.player = player

        self.hp = 2

        self.firstShootingSwitch=True
        self.lastShotTime = 0
        self.shotCooldown = 2

        self.lastBlinkTriggerTime = 0
        self.blinkTime = 0.5+(0.1*getCurrDiff())
        self.blinkStatus = False
        self._blinker = 0

        self.goAwayTimer = 0
        self.goAwayWaitSeconds = 3
        self.turnSeconds = 2
        self.goingAway = False

        self.target = [random.randint(100, 500), random.randint(100, 500)]
        self.position = [random.randint(0, 600), 700]
        # self.target = [300,300]
        # self.position = [300,300]

        self.lookDirection = 0
        self.speed = 10+(4*getCurrDiff())
        self.bulletSpeed = 5 + (2*getCurrDiff())

        self.maxDistX = math.sqrt(
            math.pow(self.position[0]-self.target[0], 2))+1e-3
        self.maxDistY = math.sqrt(
            math.pow(self.position[1]-self.target[1], 2))+1e-3

    def update(self, uptime):
        speedX = 0
        speedY = 0
        targetAngle = 180
        if not self.goingAway:
            if getDist(self.position, self.target) < 70:
                if self.firstShootingSwitch:
                    self.firstShootingSwitch=False
                    self.lastShotTime=uptime
                # stój i strzelaj,obracając się w strone gracza

                pX = (self.player.position[0]-self.position[0])
                pY = (self.player.position[1]-self.position[1])
                pAngle = math.atan2(pY, pX)
                targetAngle = math.degrees(pAngle)-90
                
                if self.lastShotTime+self.shotCooldown < uptime:
                    self.lastShotTime = uptime
                    bX = math.cos(pAngle)
                    bY = math.sin(pAngle)

                    enemyBullets.append(
                        Bullet(self.position, bX*self.bulletSpeed, bY*self.bulletSpeed, angle=math.degrees(pAngle)-90, color="r"))
            else:
                # leć do target
                wX = self.target[0]-self.position[0]
                wY = self.target[1]-self.position[1]

                targetAngle = math.degrees(math.atan2(wY, wX))-90

                speedX = (wX/self.maxDistX)*self.speed
                speedY = (wY/self.maxDistY)*self.speed
        else:
            targetAngle = self.angle
            if self.turnSeconds+self.goAwayTimer < uptime:
                wX = self.target[0]-self.position[0]
                wY = self.target[1]-self.position[1]
                targetAngle = math.degrees(math.atan2(wY, wX))-90

            if self.goAwayWaitSeconds+self.goAwayTimer < uptime:
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
        explosions.append(Explosion(self.position, scale=3))
        if getSoundState():
            arcade.play_sound(assets["death"+str(random.randint(1,3))])
        super().kill()

    def goAway(self, uptime):
        self.speed = 1
        self.goAwayTimer = uptime
        self.goingAway = True
        self.target=[random.randint(-100,700),900]

    def draw(self):
        if self.blinkStatus:
            self._blinker += 1
            if self._blinker % 3 == 0:
                super().draw()
        else:
            super().draw()
