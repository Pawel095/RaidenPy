import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Raiden Py"
WINDOW = None




bullets = []
enemies = []

class keyFlags():
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.space = False


