import arcade


class Bullet(arcade.Sprite):
    def __init__(self, position, speedX=10, speedY=10, angle=0, sprite=None, color=arcade.color.RED):
        super().__init__(sprite)
        self.position = position
        self.change_x = speedX
        self.change_y = speedY
        self.color = color
        self.angle = angle
        self.collision_radius=3

    def draw(self):
        arcade.draw_rectangle_filled(
            self.position[0], self.position[1], 50, 50, self.color, self.angle)

    def update(self):
        super().update()
