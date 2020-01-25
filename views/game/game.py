import arcade
from views.game.player import Player
from views.game.bullet import Bullet
from views.game.enemy import Enemy
from views.game.explosion import Explosion
from views.game.background import Background
import utils.globals
from utils.utilFunctions import isRemoveable
from utils.loader import assets
from utils.globals import enemyBullets, playerBullets, enemies, explosions
import time


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
        self.player = Player()
        self.background = Background()

        self.lastShotTime = -9999
        self.bulletDelay = 0.2

        self.lastEnemySpawnTime = -9999
        self.enemySpawnDelay = 2

        self.musicDuration = 1*60 + 10
        self.musicTimer=0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.play_sound(assets["defcon0"])

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.player.draw()
        [b.draw() for b in enemyBullets]
        [b.draw() for b in playerBullets]
        [e.draw() for e in enemies]
        explosions.draw()

    def on_update(self, deltaTime):
        self.uptime += deltaTime
        # play music if ended
        if self.musicDuration+self.musicTimer<self.uptime:
            arcade.play_sound(assets["defcon0"])

        self.background.update(deltaTime)

        self.player.update(self.flags)
        # [b.update() for b in playerBullets]
        playerBullets.update()
        # [b.update() for b in enemyBullets]
        enemyBullets.update()
        [e.update(self.uptime) for e in enemies]
        [e.update(deltaTime) for e in explosions]

        # player is shot?
        colided = arcade.check_for_collision_with_list(
            self.player, enemyBullets)
        if len(colided) > 0:
            for c in colided:
                c.kill()
                self.player.onHit()
                if not self.player.alive:
                    self.enemySpawnDelay = 99999
                    for e in enemies:
                        e.goAway(self.uptime)
                    # TODO: show game over text

        # enemies are shot?
        for e in enemies:
            colided = arcade.check_for_collision_with_list(e, playerBullets)
            if len(colided) > 0:
                for c in colided:
                    c.kill()
                    e.onHit(self.uptime)

        # player shoting
        if self.flags.space:
            if (self.lastShotTime+self.bulletDelay < self.uptime):
                self.lastShotTime = self.uptime
                playerBullets.append(Bullet(self.player.position, 0, 10, 90))

        # spawn enemies
        if self.lastEnemySpawnTime+self.enemySpawnDelay < self.uptime:
            enemies.append(Enemy(self.player))
            self.lastEnemySpawnTime = self.uptime

        # remove old enemy Bullets bullets
        for b in enemyBullets:
            if not isRemoveable(b.position):
                enemyBullets.remove(b)
                del b
        # remove old player bullets
        for b in playerBullets:
            if not isRemoveable(b.position):
                playerBullets.remove(b)
                del b

    def on_mouse_press(self, _x, _y, _button, _modifiers):
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
