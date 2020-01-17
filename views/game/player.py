import arcade
from utils.utilFunctions import approach

class Player(arcade.Sprite):
    def __init__(self, speed=10,slowModifier=0.1, spritePath=None):
        super().__init__(spritePath)
        self.speed = speed

    def draw(self):
        arcade.draw_rectangle_filled(
            self.position[0], self.position[1], 100, 100, arcade.color.BLACK)

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
        self.change_x=approach(self.change_x,deltaX,0.1)
        self.change_y=approach(self.change_y,deltaY,0.1)
        super().update()
