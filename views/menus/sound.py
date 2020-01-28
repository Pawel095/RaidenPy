from arcade import TextButton
from arcade.gui import Theme
import arcade
import utils.globals
from utils.menusFunctions import soundText, toggleSound




class SoundOptionsView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def __init__(self):
        super().__init__()    
        self.theme = None
        self.background = None
        self.screen_header = "Sound Effects"
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
        soundToggleButton = SoundToggle(self, 300, 335, 190, 50, theme=self.theme)
        optionsButton = ReturnButton(self, 300, 240, 190, 50, theme=self.theme)
        self.button_list.append(soundToggleButton)
        self.button_list.append(optionsButton)

        utils.menusFunctions.app_buttons.append(soundToggleButton)
        utils.menusFunctions.app_buttons.append(optionsButton)



    def setup(self):
        self.setup_theme()
        self.set_buttons()
        self.background = arcade.load_texture('assets/background.jpg')

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        arcade.draw_texture_rectangle(utils.globals.SCREEN_WIDTH // 2, utils.globals.SCREEN_HEIGHT // 2,
                                      utils.globals.SCREEN_WIDTH, utils.globals.SCREEN_HEIGHT, self.background)
        arcade.draw_text(self.screen_header, self.screen_header_x, self.screen_header_y, arcade.color.ALICE_BLUE, self.screen_header_font_size, align="center", anchor_x="center", anchor_y="center")
        [button.draw() for button in self.button_list]

    def on_update(self, delta_time):
        self.updateText()

    def updateText(self):
        self.screen_header = utils.languagePack.soundText[utils.menusFunctions.currentLanguage]
        



class SoundToggle(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.menusFunctions.soundText, theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True
        

    def on_release(self):
        if self.pressed:
            #change sound to on/off
            utils.menusFunctions.toggleSound()
            self.update()
            # self.game.pause = False
            self.pressed = False

    def update(self):
        utils.menusFunctions.soundLang()
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.menusFunctions.soundText, theme=self.theme)




class ReturnButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.optionsText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
        
    def on_release(self):
        if self.pressed:
            utils.globals.WINDOW.show_view(utils.views.options_view)
            self.pressed = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.optionsText[utils.menusFunctions.currentLanguage], theme=self.theme)

    