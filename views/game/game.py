import arcade
from views.game.player import Player
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
        self.ball = Player()
        self.flags = utils.flags.keyFlags()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.play_sound(assets["defcon0"])

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_update(self, deltaTime):
        self.ball.update(self.flags)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # arcade.close_window()
        rv = randomView()
        self.window.show_view(rv)

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
