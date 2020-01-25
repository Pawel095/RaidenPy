from arcade import TextButton
from arcade.gui import Theme
import arcade
import utils.globals
import utils.views





class MainMenu(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def __init__(self):
        super().__init__()    
        self.theme = None
        self.background = None
        self.screen_header = "Raiden Py"
        self.screen_header_font_size = 60
        self.screen_header_x = 300
        self.screen_header_y = 450
        self.setup()
        
        

    def set_button_textures(self):
        normal = "assets/normal.png"
        hover = "assets/hover.png"
        clicked = "assets/clicked.png"
        locked = "assets/locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.theme = Theme()
        self.theme.set_font(24, arcade.color.WHITE)
        self.set_button_textures()

    def set_buttons(self):
        self.button_list.append(PlayButton(self, 300, 380, 190, 50, theme=self.theme))
        self.button_list.append(OptionsButton(self, 300, 310, 190, 50, theme=self.theme))
        self.button_list.append(ExitButton(self, 300, 240, 190, 50, theme=self.theme))

    def setup(self):
        self.setup_theme()
        self.set_buttons()
        self.background = arcade.load_texture('assets/background.jpg')

    def on_draw(self):
        arcade.start_render()
        
        super().on_draw()
        arcade.draw_texture_rectangle(utils.globals.SCREEN_WIDTH // 2, utils.globals.SCREEN_HEIGHT // 2,
                                      utils.globals.SCREEN_WIDTH, utils.globals.SCREEN_HEIGHT, self.background)
        arcade.draw_text(self.screen_header, self.screen_header_x, self.screen_header_y, arcade.color.WHITE, self.screen_header_font_size, align="center", anchor_x="center", anchor_y="center")
        [button.draw() for button in self.button_list]



class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Play", font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            utils.globals.WINDOW.show_view(utils.views.game_view)
            # self.game.pause = False


class OptionsButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Options", font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game


    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False 
            utils.globals.WINDOW.show_view(utils.views.options_view)


class ExitButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Exit", font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
        
    def on_release(self):
        if self.pressed:
            self.pressed = False
            arcade.close_window()
