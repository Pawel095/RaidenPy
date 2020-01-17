import arcade


class loader():
    def __init__(self):
        self.data = {}

    def load(self):
        self.data["defcon0"] = arcade.load_sound("assets/Defcon_Zero.wav")

    def get(self, key):
        try:
            ret = self.data[key]
        except KeyError as e:
            print(e)
        else:
            return ret
