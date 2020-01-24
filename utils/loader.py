import arcade
import threading

assets = {}
loadingFinished = False


class worker(threading.Thread):
    def __init__(self, loadFunc, path, key,args=None):
        super().__init__()
        self.loadFunc = loadFunc
        self.path = path
        self.key = key
        self.args=args

    def run(self):
        if self.args is not None:
            assets[self.key] = self.loadFunc(self.path,*self.args)
        else:
            assets[self.key] = self.loadFunc(self.path)


class Loader():
    def load(self):
        threads = []
        threads.extend(
            [worker(arcade.load_sound, "assets/Defcon_Zero.wav", "defcon0"),
             worker(arcade.load_texture, "assets/enemy1.png", "enemy1"),
             worker(arcade.load_texture, "assets/enemy2.png", "enemy2"),
             worker(arcade.load_texture, "assets/enemy3.png", "enemy3"),
             worker(arcade.load_texture, "assets/laser1.png", "laser1"),
             worker(arcade.load_texture, "assets/laser2.png", "laser2"),
             worker(arcade.load_texture, "assets/player.png", "player"),
             worker(arcade.load_sound,"assets/laserShot1.wav","shot1"),
             worker(arcade.load_sound,"assets/laserShot2.wav","shot2"),
             worker(arcade.load_sound,"assets/laserShot3.wav","shot3"),
             worker(arcade.load_sound,"assets/laserShot4.wav","shot4"),
             worker(arcade.load_sound,"assets/laserShot5.wav","shot5"),
             worker(arcade.load_sound,"assets/laserShot6.wav","shot6"),
             worker(arcade.load_spritesheet,"assets/explosion.png","explosion",[64,64,4,16])
             ])
        [t.start() for t in threads]
        [t.join() for t in threads]
        loadingFinished = True

        if loadingFinished:
            pass

    def get(self, key):
        try:
            ret = assets[key]
        except KeyError as e:
            print(e)
        else:
            return ret
