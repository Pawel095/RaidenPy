import arcade


class Bullet(arcade.Sprite):
    def __init__(self, position, speedX=10, speedY=10, sprite=None, color=arcade.color.RED):
        super().__init__(sprite)
        self.position = position
        self.change_x = speedX
        self.change_y = speedY
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(
            self.position[0], self.position[1], 50, 50, self.color, self.position[1])

    def update(self):
        super().update()
