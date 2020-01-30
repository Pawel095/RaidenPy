from arcade import TextButton
from arcade.gui import Theme
import arcade
import utils.globals
import utils.views
import utils.languagePack
import utils.menusFunctions


class Options(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def __init__(self):
        super().__init__()    
        self.theme = None
        self.background = None
        self.screen_header = "Options"
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
        diffButton = DifficultyButton(self, 300, 380, 190, 50, theme=self.theme)
        soundButton = SoundButton(self, 300, 310, 190, 50, theme=self.theme)
        keysButton = KeyBindsButton(self, 300, 240, 190, 50, theme=self.theme)
        langButton = LanguageButton(self, 300, 170, 190, 50, theme=self.theme)
        menuButton = ReturnButton(self, 300, 95, 190, 50, theme=self.theme)
        self.button_list.append(diffButton)
        self.button_list.append(soundButton)
        self.button_list.append(keysButton)
        self.button_list.append(langButton)
        self.button_list.append(menuButton)

        utils.menusFunctions.app_buttons.append(diffButton)
        utils.menusFunctions.app_buttons.append(soundButton)
        utils.menusFunctions.app_buttons.append(keysButton)
        utils.menusFunctions.app_buttons.append(langButton)
        utils.menusFunctions.app_buttons.append(menuButton)

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
        self.screen_header = utils.languagePack.optionsText[utils.menusFunctions.currentLanguage]


class DifficultyButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.difficultyText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            utils.globals.WINDOW.show_view(utils.views.difficulty_view)
            # self.game.pause = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.difficultyText[utils.menusFunctions.currentLanguage], theme=self.theme)


class SoundButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.soundText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            utils.globals.WINDOW.show_view(utils.views.sound_view)
            # self.game.pause = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.soundText[utils.menusFunctions.currentLanguage], theme=self.theme)

class KeyBindsButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.keybindsText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game


    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            utils.globals.WINDOW.show_view(utils.views.keybinds_view)
            self.pressed = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.keybindsText[utils.menusFunctions.currentLanguage], theme=self.theme)


class LanguageButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.languageText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            utils.globals.WINDOW.show_view(utils.views.language_view)
            self.pressed = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.languageText[utils.menusFunctions.currentLanguage], theme=self.theme)

class ReturnButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.mainMenuText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
        
    def on_release(self):
        if self.pressed:
            utils.globals.WINDOW.show_view(utils.views.main_menu)
            self.pressed = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.mainMenuText[utils.menusFunctions.currentLanguage], theme=self.theme)