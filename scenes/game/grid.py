"""list used for pathfinding, optimizations"""

import pygame as pg

class Grid:
    def __init__(self):
        # BLOCK = 32px, MAP = 128*128 blocks, BORDER 1 block
        self.GRID = [[[] for x in range(128)] for y in range(128)] 
        self.GRID_PATHFINDING = [[0 for x in range(128)] for y in range(128)] 
        self.SIZE = [128,128]

    def loop(self):
        pass

GRID = Grid()
