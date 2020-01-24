from views.game.player import Player

class keyFlags():
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.space = False


bullets = []
enemies = []
player = Player()
