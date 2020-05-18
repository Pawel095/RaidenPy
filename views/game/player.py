import arcade
from utils.utilFunctions import approach, clampToScreen
from utils.loader import assets
from utils.globals import explosions, enemies
from views.game.explosion import Explosion


class Player(arcade.Sprite):
    def __init__(self, speed=10, slowModifier=0.1, scale=0.7):
        super().__init__(None)
        self.set_position(100, 100)
        self.speed = speed
        self.collision_radius = 100
        self.texture = assets["player"]
        self.scale = scale
        self.alive = True

    def draw(self):
        if self.alive:
            super().draw()

    def onHit(self):
        self.alive = False
        arcade.play_sound(assets["playerDeath"])
        explosions.append(Explosion(self.position, 2))

    def update(self, flags):
        if self.alive:
            deltaX = 0
            deltaY = 0
            if flags.left:
                deltaX += -1
            if flags.right:
                deltaX += 1
            if flags.up:
                deltaY += 1
            if flags.down:
                deltaY += -1
            deltaX *= self.speed
            deltaY *= self.speed
            self.change_x = approach(self.change_x, deltaX, 0.1)
            self.change_y = approach(self.change_y, deltaY, 0.1)
            super().update()
            clampToScreen(self)
