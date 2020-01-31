from arcade import TextButton
from arcade.gui import Theme
import arcade
import utils.globals
import utils.views
import utils.menusFunctions
import database.dbfuns





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
        if(database.dbfuns.conn == None):
                database.dbfuns.connectDB()
        

    def set_button_textures(self):
        normal = "assets/normal.png"
        hover = "assets/hover.png"
        clicked = "assets/clicked.png"
        locked = "assets/locked.png"
        self.theme.add_button_textures(normal, hover, clicked, locked)

    def setup_theme(self):
        self.theme = Theme()
        self.theme.set_font(20, arcade.color.WHITE)
        self.set_button_textures()

    def set_buttons(self):
        playButton = PlayButton(self, 300, 380, 240, 50, theme=self.theme)
        optionsButton = OptionsButton(self, 300, 310, 240, 50, theme=self.theme)
        leaderboardButton = LeaderboardButton(self, 300, 240, 240, 50, theme=self.theme)
        exitButton = ExitButton(self, 300, 170, 240, 50, theme=self.theme)

        self.button_list.append(playButton)
        self.button_list.append(optionsButton)
        self.button_list.append(leaderboardButton)
        self.button_list.append(exitButton)

        utils.menusFunctions.app_buttons.append(playButton)
        utils.menusFunctions.app_buttons.append(optionsButton)
        utils.menusFunctions.app_buttons.append(leaderboardButton)
        utils.menusFunctions.app_buttons.append(exitButton)

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
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.playText[utils.menusFunctions.currentLanguage], font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game
       

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            
            utils.globals.WINDOW.show_view(utils.views.setName_view)
            # self.game.pause = False

    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.playText[utils.menusFunctions.currentLanguage], theme=self.theme)


class OptionsButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.optionsText[utils.menusFunctions.currentLanguage], font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game


    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            utils.globals.WINDOW.show_view(utils.views.options_view)
    
    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.optionsText[utils.menusFunctions.currentLanguage], theme=self.theme)


class LeaderboardButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.leaderboardText[utils.menusFunctions.currentLanguage], font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True

    def on_release(self):
        if self.pressed:
            self.pressed = False
            

            database.dbfuns.selectScores()
            utils.globals.WINDOW.show_view(utils.views.leaderboard_view)
    
    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.leaderboardText[utils.menusFunctions.currentLanguage], theme=self.theme)

class ExitButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text=utils.languagePack.exitText[utils.menusFunctions.currentLanguage], font_size=18, theme=None):
        super().__init__(x, y, width, height, text, font_size, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
        
    def on_release(self):
        if self.pressed:
            self.pressed = False
            database.dbfuns.closeConnection()
            arcade.close_window()
    
    def update(self):
        super().__init__(self.center_x, self.center_y, self.width, self.height, text=utils.languagePack.exitText[utils.menusFunctions.currentLanguage], theme=self.theme)
