"""background image"""

import pygame as pg
import uuid
from window import WINDOW

class Map:
    def __init__(self):
        self.POS = [0, 0]
        self.IMAGE = pg.image.load("scenes/game/assets/map.png")

    def change_pos(self, pos):
        self.POS = pos

    def add_pos(self, pos):
        self.POS = [a + b for a, b in zip(self.POS, pos)]

    def draw(self, camera_pos=(0,0)):
        WINDOW.SCREEN.blit(self.IMAGE, (self.POS[0]-camera_pos[0], self.POS[1]-camera_pos[1]))

    def loop(self, camera_pos=(0,0)):
        self.draw(camera_pos)

MAP = Map()
