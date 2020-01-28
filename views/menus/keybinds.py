from arcade import TextButton
from arcade.gui import Theme
import arcade
import utils.globals
import utils.views
import utils.menusFunctions
import utils.languagePack


class KeybindsOptionsView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def __init__(self):
        super().__init__()    
        self.theme = None
        self.background = None
        self.screen_header = utils.languagePack.keybindsText[utils.menusFunctions.currentLanguage]
        self.movementText = utils.languagePack.movementText[utils.menusFunctions.currentLanguage]
        self.shootText = utils.languagePack.shootText[utils.menusFunctions.currentLanguage]
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

    def set_button_textures_disabled(self):
        normal = "assets/normalDisabled.png"
        hover = "assets/hoverDisabled.png"
        clicked = "assets/clickedDisabled.png"
        locked = "assets/lockedDisabled.png"
        self.themeDisabled.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.theme = Theme()
        self.themeDisabled = Theme()
        self.theme.set_font(24, arcade.color.WHITE)
        self.themeDisabled.set_font(24, arcade.color.WHITE)
        self.set_button_textures()
        self.set_button_textures_disabled()

    def set_buttons(self):
        mvButton = MovementButton(self, 400, 380, 190, 50, theme=self.theme)
        shootButton = ShootButton(self, 400, 310, 190, 50, theme=self.themeDisabled)
        optionsButton = ReturnButton(self, 300, 240, 190, 50, theme=self.theme)

        self.button_list.append(mvButton)
        self.button_list.append(shootButton)
        self.button_list.append(optionsButton)

        utils.menusFunctions.app_buttons.append(mvButton)
        utils.menusFunctions.app_buttons.append(shootButton)
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
        arcade.draw_text(utils.languagePack.movementText[utils.menusFunctions.currentLanguage], 200, 380, arcade.color.ALICE_BLUE, 28, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(utils.languagePack.shootText[utils.menusFunctions.currentLanguage], 200, 310, arcade.color.ALICE_BLUE, 28, align="center", anchor_x="center", anchor_y="center")
        [button.draw() for button in self.button_list]

    def on_update(self, delta_time):
        self.updateText()

    def updateText(self):
        self.screen_header = utils.languagePack.keybindsText[utils.menusFunctions.currentLanguage]
        self.movementText = utils.languagePack.movementText[utils.menusFunctions.currentLanguage]
        self.shootText = utils.languagePack.shootText[utils.menusFunctions.currentLanguage]



class MovementButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.menusFunctions.bindsText, theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            utils.menusFunctions.changeKeybinds()
            self.update()
            # self.game.pause = False

    def update(self):
        utils.menusFunctions.keybindsLang()
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.menusFunctions.bindsText, theme=self.theme)


class ShootButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.spacebarText[utils.menusFunctions.currentLanguage], theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            # self.game.pause = False
    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.spacebarText[utils.menusFunctions.currentLanguage], theme=self.theme)



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
