"""
window module
"""

import pygame as pg

class Window:
    def __init__(self):    
        # PARAMETERS
        self.WIDTH = 960
        self.HEIGHT = 540
        self.SCALE = 2
        self.FPS = 60
        self.CAPTION = ""
        self.IMAGE = ""

        self.LOOP = True
        self.EVENTS = []

        pg.init()
        pg.display.set_caption(self.CAPTION)
        if self.IMAGE != "":
            icon = pg.image.load(self.IMAGE)
            pg.display.set_icon(icon)

        # FIRST SCREEN THAT IS BLITTED, ALSO SCLAED, USED FOR GAME
        self.SCREEN = pg.Surface([self.WIDTH, self.HEIGHT])
        # SECOND SCREEN THAT IS BLITTED, NOT SCALED, USED FOR UI
        self.SCREENUI = pg.Surface([self.WIDTH*self.SCALE, self.HEIGHT*self.SCALE], pg.SRCALPHA)

        self.WINDOW = pg.display.set_mode((int(self.WIDTH * self.SCALE), int(self.HEIGHT * self.SCALE))) #pg.FULLSCREEN
        self.CLOCK = pg.time.Clock()

    def loop(self):
        """
        Used for scene manager compatibility.
        """
        self.LOOP = False

    def update(self):
        """
        To be put in main loop.
        """
        pg.transform.scale(self.SCREEN, (int(self.WIDTH * self.SCALE), int(self.HEIGHT * self.SCALE)), self.WINDOW)
        self.WINDOW.blit(self.SCREENUI, (0,0))

        self.CLOCK.tick(self.FPS)
        pg.display.update()
        self.EVENTS = pg.event.get()

WINDOW = Window()
