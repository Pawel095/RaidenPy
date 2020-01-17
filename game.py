import arcade


class MenuView(arcade.View):
    def setupFlags(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def on_show(self):
        self.setupFlags()
        arcade.set_background_color(arcade.color.WHITE)
        defcon0 = arcade.load_sound("assets/Defcon_Zero.wav")
        arcade.play_sound(defcon0)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen - click to advance", 600/2,
                         600/2, arcade.color.BLACK, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        arcade.close_window()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.left = True
        elif key == arcade.key.RIGHT:
            self.right = True
        elif key == arcade.key.UP:
            self.up = True
        elif key == arcade.key.DOWN:
            self.down = True

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
