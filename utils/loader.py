import arcade
import threading

assets = {}
loadingFinished = False


class worker(threading.Thread):
    def __init__(self, loadFunc, path, key):
        super().__init__()
        self.loadFunc = loadFunc
        self.path = path
        self.key = key

    def run(self):
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
             worker(arcade.load_texture, "assets/player.png", "player")
             ])
        [t.start() for t in threads]
        [t.join() for t in threads]
        loadingFinished = True
        print(assets)

        if loadingFinished:
            pass

    def get(self, key):
        try:
            ret = assets[key]
        except KeyError as e:
            print(e)
        else:
            return ret
