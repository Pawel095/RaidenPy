import arcade
from views.game.player import Player
from views.game.bullet import Bullet
from views.game.enemy import Enemy
import utils.globals
from utils.loader import assets
from utils.globals import enemyBullets, playerBullets, enemies, player


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
        self.flags = utils.globals.keyFlags()
        self.uptime = 0

        self.lastShotTime = -9999
        self.bulletDelay = 0.2

        self.lastEnemySpawnTime = -9999
        self.enemySpawnDelay = 4

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.play_sound(assets["defcon0"])

    def on_draw(self):
        arcade.start_render()
        player.draw()
        [b.draw() for b in enemyBullets]
        [b.draw() for b in playerBullets]
        [e.draw() for e in enemies]

    def on_update(self, deltaTime):
        self.uptime += deltaTime

        player.update(self.flags)
        [b.update() for b in playerBullets]
        [b.update() for b in enemyBullets]
        [e.update(self.uptime) for e in enemies]

        colided = arcade.check_for_collision_with_list(player, enemyBullets)
        if len(colided) > 0:
            print(colided)

        # player shoting
        if self.flags.space:
            if (self.lastShotTime+self.bulletDelay < self.uptime):
                self.lastShotTime = self.uptime
                playerBullets.append(Bullet(player.position, 0, 10, 90))

        # spawn enemies
        if self.lastEnemySpawnTime+self.enemySpawnDelay < self.uptime:
            enemies.append(Enemy())
            self.lastEnemySpawnTime = self.uptime

        # remove old bullets
        for b in enemyBullets:
            if b.position[0] > 700 or b.position[1] > 700:
                enemyBullets.remove(b)
                del b

        for b in playerBullets:
            if b.position[0] > 700 or b.position[1] > 700:
                playerBullets.remove(b)
                del b

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
