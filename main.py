"""
start of program, scene manager
"""

from window import WINDOW
from scenes.game.game import GAME

class Main:
    def __init__(self):
        self.SCENES = [WINDOW]

    def scene_prev(self):
        self.SCENES.pop()

    def scene_next(self, scene):
        self.SCENES.append(scene)

    def current_scene(self):
        return self.SCENES[-1]

    def loop(self):
        """
        main loop
        """
        while WINDOW.LOOP:
            self.current_scene().loop()
            WINDOW.update()

MAIN = Main()
MAIN.scene_next(GAME)
MAIN.loop()
