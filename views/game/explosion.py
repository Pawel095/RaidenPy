import arcade
from utils.loader import assets
import math


class Explosion(arcade.Sprite):
    def __init__(self,position=[0,0], scale=2):
        super().__init__()
        self.position = position
        self.current_texture = 0
        self.textures = assets["explosion"]
        for t in self.textures:
            t.scale = scale
        
        self.texture = self.textures[0]
        self.scale = scale
        # 16 fps
        self.deltaFrame = 0.0625
        self.deltaTime = 0

    def update(self, delta):
        self.deltaTime += delta
        frames = math.floor(self.deltaTime/self.deltaFrame)
        if frames > 0:
            self.deltaTime -= self.deltaFrame*frames
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.texture = self.textures[self.current_texture]
            else:
                self.kill()

    def draw(self):
        super().draw()
