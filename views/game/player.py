import arcade
from utils.utilFunctions import approach,clampToScreen
from utils.loader import assets


class Player(arcade.Sprite):
    def __init__(self, speed=10, slowModifier=0.1,  scale=0.5):
        super().__init__(None)
        self.set_position(100, 100)
        self.speed = speed
        self.collision_radius = 100
        self._texture = assets["player"]
        if self._texture:
            self.textures = [self._texture]
            self._width = self._texture.width*scale
            self._height = self._texture.height*scale
            self._texture.scale = scale

    def draw(self):
        super().draw()
    
    def onHit(self):
        pass

    def update(self, flags):
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