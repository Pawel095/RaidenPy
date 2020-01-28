import arcade
from utils.loader import assets
from utils.menusFunctions import getSoundState()
import random

class Bullet(arcade.Sprite):
    def __init__(self, position, speedX=10, speedY=10, angle=0,scale=1, color="b"):
        super().__init__(None)
        self.position = position
        self.change_x = speedX
        self.change_y = speedY
        self.color = color
        self.angle = angle
        if color == "b":
            self.texture = assets["laser1"]
        else:
            self.texture = assets["laser2"]
        if getSoundState():
            arcade.play_sound(assets["shot"+str(random.randint(1,6))])

    def draw(self):
        super().draw()
        # arcade.draw_rectangle_filled(
        #     self.position[0], self.position[1], 50, 50, self.color, self.angle)

    def update(self):
        super().update()
