"""game camera, draws game objects"""

import pygame as pg

class Camera:
    def __init__(self):
        self.POS = [0, 0]
        self.GRID_POS = [self.POS[1]//32, self.POS[0]//32]

    def change_pos(self, pos, objects):
        self.POS = pos
        self.GRID_POS = [self.POS[0]//32, self.POS[1]//32]
        for obj in objects:
            obj.new_rectscreen()

    def add_pos(self, pos, objects):
        self.POS = [a + b for a, b in zip(self.POS, pos)]
        self.GRID_POS = [self.POS[0]//32, self.POS[1]//32]
        for obj in objects:
            obj.new_rectscreen()

    def loop(self, grid):
        for i in grid:
            for j in i:
                for k in j:
                    k.draw()

CAMERA = Camera()
