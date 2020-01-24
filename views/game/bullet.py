import arcade
from utils.loader import assets

class Bullet(arcade.Sprite):
    def __init__(self, position, speedX=10, speedY=10, angle=0,scale=1, color="b"):
        super().__init__(None)
        self.position = position
        self.change_x = speedX
        self.change_y = speedY
        self.color = color
        self.angle = angle
        if color == "b":
            self._texture = assets["laser1"]
        else:
            self.texture = assets["laser2"]
        if self._texture:
            self.textures = [self._texture]
            self._width = self._texture.width*scale
            self._height = self._texture.height*scale
            self._texture.scale = scale

    def draw(self):
        super().draw()
        # arcade.draw_rectangle_filled(
        #     self.position[0], self.position[1], 50, 50, self.color, self.angle)

    def update(self):
        super().update()
