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
        assets[self.key]=self.loadFunc(self.path)


class Loader():
    def load(self):
        threads = []
        threads.append(
            worker(arcade.load_sound, "assets/Defcon_Zero.wav", "defcon0"))
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
