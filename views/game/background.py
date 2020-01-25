import arcade
import random
from utils.globals import WIDTH, HEIGHT


class Particle():
    """mały obracający się biały kwadrat"""

    def __init__(self, position=[random.randint(0, WIDTH), HEIGHT+100]):
        self.change_x = random.randrange(-2,2)
        self.change_y = random.randrange(-400,-10)
        self.angle_change = random.randrange(-20, 20)
        self.position = position
        self.angle = random.randint(0, 360)
        self.size = random.randint(1, 7)

    def update(self, deltaT):
        self.position[0] += self.change_x*deltaT
        self.position[1] += self.change_y*deltaT
        self.angle += self.angle_change*deltaT

    def draw(self):
        arcade.draw_rectangle_filled(self.position[0],
                                     self.position[1],
                                     self.size,
                                     self.size,
                                     arcade.color.WHITE,
                                     self.angle)


class Background():
    def __init__(self):
        self.particles = []
        for _ in range(10):
            self.particles.append(
                Particle([random.randint(0, WIDTH), random.randrange(0, HEIGHT)]))

    def draw(self):
        [p.draw() for p in self.particles]

    def update(self,deltaT):
        [p.update(deltaT) for p in self.particles]