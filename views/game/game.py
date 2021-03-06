import arcade
from views.game.player import Player
from views.game.bullet import Bullet
from views.game.enemy import Enemy
from views.game.explosion import Explosion
from views.game.background import Background
import utils.globals
from utils.utilFunctions import isRemoveable
from utils.loader import assets
from utils.globals import enemyBullets, playerBullets, enemies, explosions, getPlayerKills
from utils.menusFunctions import getSoundState, languageList, getCurrLang, getCurrDiff, difficultyList, getCurrKeybinds
from utils.languagePack import gameOverText, gameOverInfoText
import time
from database.dbfuns import insertValues, saveChanges, closeConnection
import random


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.flags = utils.globals.keyFlags()
        self.uptime = 0
        self.player = Player()
        self.background = Background()

        self.lastShotTime = 0
        self.bulletDelay = 0.4

        self.lastEnemySpawnTime = 0
        self.enemySpawnDelay = 2

        self.musicDuration = 1*60 + 10
        self.musicTimer = -7777

        self.gameOverTimer = 0
        self.gameOverTextTime = 1
        self.gameOver = False

        self.lastScoreUpdateTime = 0
        self.lastScoreUpdateDelay = 0.4
        self.score = 0
        self.textScore = "0000000000"

    def setNickname(self, name):
        self.playerName = name

    def on_gameOver(self):
        if self.playerName == "":
            self.playerName = "Anon"
        insertValues(self.playerName, self.score)
        saveChanges()
        closeConnection()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        # arcade.play_sound(assets["defcon0"])
        self.enemySpawnDelay = 2.5-(0.5*getCurrDiff())
        self.uptime = 0

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        [b.draw() for b in enemyBullets]
        [b.draw() for b in playerBullets]
        [e.draw() for e in enemies]
        self.player.draw()
        explosions.draw()

        arcade.draw_text(self.textScore, 10, 570, arcade.color.WHITE,
                         20, align="center")

        if self.gameOver and self.gameOverTimer+self.gameOverTextTime < self.uptime:
            arcade.draw_text(gameOverText[getCurrLang()], 300, 420, arcade.color.WHITE_SMOKE, font_size=40,
                             align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text(gameOverInfoText[getCurrLang()], 300, 250, arcade.color.WHITE_SMOKE,
                             font_size=20, align="center", anchor_x="center", anchor_y="center")

    def on_update(self, deltaTime):
        self.uptime += deltaTime

        # play music if enabled
        if getSoundState():
            if self.musicDuration+self.musicTimer < self.uptime:
                self.musicTimer = self.uptime
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
                    self.gameOver = True
                    if self.gameOverTimer == 0:
                        self.on_gameOver()
                    self.gameOverTimer = self.uptime

        # enemies are shot?
        for e in enemies:
            colided = arcade.check_for_collision_with_list(e, playerBullets)
            if len(colided) > 0:
                for c in colided:
                    c.kill()
                    e.onHit(self.uptime)

        # player shoting
        if self.flags.space and not self.gameOver:
            if (self.lastShotTime+self.bulletDelay < self.uptime):
                self.lastShotTime = self.uptime
                playerBullets.append(
                    Bullet(self.player.position, 0, 10, 90))

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

        # update score
        if not self.gameOver:
            if self.lastScoreUpdateTime + self.lastScoreUpdateDelay < self.uptime:
                self.score = int(self.uptime*1000+getPlayerKills()*10000)
                self.textScore = str(self.score).zfill(10)
                self.lastScoreUpdateTime = self.uptime

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if self.gameOver and self.gameOverTimer+self.gameOverTextTime < self.uptime:
            arcade.close_window()

        if getCurrKeybinds() == 1:
            if key == arcade.key.A:
                self.flags.left = True
            if key == arcade.key.D:
                self.flags.right = True
            if key == arcade.key.W:
                self.flags.up = True
            if key == arcade.key.S:
                self.flags.down = True
        else:
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

        # if key == arcade.key.ESCAPE:
        #     arcade.close_window()

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if getCurrKeybinds() == 1:
            if key == arcade.key.A:
                self.flags.left = False
            if key == arcade.key.D:
                self.flags.right = False
            if key == arcade.key.W:
                self.flags.up = False
            if key == arcade.key.S:
                self.flags.down = False
        else:
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
