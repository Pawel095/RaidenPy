import arcade
from views.game.player import Player
from views.game.bullet import Bullet
import utils.flags
from utils.loader import assets


class randomView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over - press ESCAPE to advance",
                         300, 300, arcade.color.WHITE, 20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arcade.close_window()


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.flags = utils.flags.keyFlags()
        self.uptime = 0
        self.lastShotTime = -9999
        self.bullets = []
        self.bulletDelay=0.2

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.play_sound(assets["defcon0"])

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        [b.draw() for b in self.bullets]

    def on_update(self, deltaTime):
        self.uptime += deltaTime

        self.player.update(self.flags)
        for b in self.bullets:
            b.update()
            if b.position[0]>700 or b.position[1]>700:
                self.bullets.remove(b)

        if self.flags.space:
            if (self.lastShotTime+self.bulletDelay<self.uptime):
                self.lastShotTime=self.uptime
                self.bullets.append(Bullet(self.player.position,0,10))
                

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # arcade.close_window()
        # rv = randomView()
        # self.window.show_view(rv)
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.flags.left = True
        if key == arcade.key.RIGHT:
            self.flags.right = True
        if key == arcade.key.UP:
            self.flags.up = True
        if key == arcade.key.DOWN:
            self.flags.down = True

        if key == arcade.key.SPACE:
            self.flags.space = True

        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT:
            self.flags.left = False
        if key == arcade.key.RIGHT:
            self.flags.right = False
        if key == arcade.key.UP:
            self.flags.up = False
        if key == arcade.key.DOWN:
            self.flags.down = False

        if key == arcade.key.SPACE:
            self.flags.space = False
