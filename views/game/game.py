import arcade
from views.game.player import Player
import utils.flags


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ball = Player()
        self.flags = utils.flags.keyFlags()

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        # defcon0 = arcade.load_sound("assets/Defcon_Zero.wav")
        # arcade.play_sound(defcon0)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_update(self, deltaTime):
        self.ball.update(self.flags)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arcade.close_window()

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
