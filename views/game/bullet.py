import arcade


class Bullet(arcade.Sprite):
    def __init__(self,position, speedX=10, speedY=10, sprite=None):
        super().__init__(sprite)
        self.position=position
        self.change_x=speedX
        self.change_y=speedY

    def draw(self):
        arcade.draw_rectangle_filled(self.position[0],self.position[1],50,50,arcade.color.RED,self.position[0])

    def update(self):
        super().update()
        
