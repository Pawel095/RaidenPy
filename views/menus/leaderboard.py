from arcade import TextButton
from arcade.gui import Theme
import arcade
import utils.globals
import database.dbfuns




class LeaderboardView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def __init__(self):
        super().__init__()    
        self.theme = None
        self.background = None
        self.playerText = utils.languagePack.playerText[utils.menusFunctions.currentLanguage]
        self.scoreText = utils.languagePack.scoreText[utils.menusFunctions.currentLanguage]
        
        self.setup()
        

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
        
        optionsButton = ReturnButton(self, 300, 210, 240, 50, theme=self.theme)

        self.button_list.append(optionsButton)

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
        arcade.draw_text('#', 50, 500, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(self.playerText, 200, 500, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(self.scoreText, 450, 500, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("1", 50, 430, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("2", 50, 360, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("3", 50, 290, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(database.dbfuns.data[0]['playername'], 200, 430, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(database.dbfuns.data[0]['score']), 450, 430, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(database.dbfuns.data[1]['playername'], 200, 360, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(database.dbfuns.data[1]['score']), 450, 360, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(database.dbfuns.data[2]['playername'], 200, 290, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text(str(database.dbfuns.data[2]['score']), 450, 290, arcade.color.ALICE_BLUE, 30, align="center", anchor_x="center", anchor_y="center")
        [button.draw() for button in self.button_list]

    def on_update(self, delta_time):
        self.updateText()
        

    def updateText(self):
        self.playerText = utils.languagePack.playerText[utils.menusFunctions.currentLanguage]
        self.scoreText = utils.languagePack.scoreText[utils.menusFunctions.currentLanguage]
        
        






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

    