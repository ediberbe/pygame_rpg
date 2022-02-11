"""templates for future classes"""

import uuid
from animation import *
from movement import *
from state import *

from window import WINDOW
from scenes.game.camera import CAMERA
from scenes.game.grid import GRID

class BasicObject:
    def __init__(self, pos=[0*32+15,0*32+31], size=[32,32], sizescreen=[32,32], offset=[0,0]):
        self.ID = uuid.uuid4()

        self.POS = pos
        self.GRID_POS = (self.POS[1]//32, self.POS[0]//32)
        GRID.GRID[self.GRID_POS[0]][self.GRID_POS[1]].append(self)

        self.SIZE = size
        self.SIZESCREEN = sizescreen
        self.OFFSET = offset

        self.RECT = None
        self.new_rect()
        self.RECTSCREEN = None
        self.new_rectscreen()

        self.IS_OBSTACLE = True
        self.AM = AnimationManager(WINDOW.SCREEN)
        self.SM = StateManager()

        self.load_animations()
        self.load_states()

    def load_animations(self):
        return None

    def load_states(self):
        return None

    def change_pos_to_block(self, x, y):
        self.POS = [x*32+15, y*32+31]
        self.update_grid()
        self.new_rect()
        self.new_rectscreen()

    def update_grid(self):
        if self.GRID_POS != (self.POS[1]//32, self.POS[0]//32):
            GRID.GRID[self.GRID_POS[0]][self.GRID_POS[1]].remove(self)
            self.GRID_POS = (self.POS[1]//32, self.POS[0]//32)
            GRID.GRID[self.GRID_POS[0]][self.GRID_POS[1]].append(self)

    def new_rect(self):
        self.RECT = pg.Rect(self.POS[0]-self.SIZE[0]//2+1, self.POS[1]-self.SIZE[1]+1, self.SIZE[0], self.SIZE[1])

    def new_rectscreen(self):
        self.RECTSCREEN = pg.Rect(self.POS[0]-self.SIZESCREEN[0]//2+1-CAMERA.POS[0], self.POS[1]-self.SIZESCREEN[1]+1-CAMERA.POS[1], self.SIZESCREEN[0], self.SIZESCREEN[1])

    def click(self, is_down, mouse_pos):
        return None

    def rclick(self, is_down, mouse_pos):
        return None

    def draw(self):
        # CLICK BOX
        pg.draw.rect(WINDOW.SCREEN, (0,255,0), self.RECTSCREEN)
        # COLLISION BOX
        pg.draw.rect(WINDOW.SCREEN, (255,0,0), pg.Rect(self.POS[0]-self.SIZE[0]//2+1-CAMERA.POS[0], self.POS[1]-self.SIZE[1]+1-CAMERA.POS[1], self.SIZE[0], self.SIZE[1]))
        # ANIMATION
        self.AM.loop((self.POS[0]-self.SIZESCREEN[0]//2+1-CAMERA.POS[0]+self.OFFSET[0],self.POS[1]-self.SIZESCREEN[1]+1-CAMERA.POS[1]+self.OFFSET[1]))

    def loop(self):
        return None

class Panel:
    def __init__(self, pos=(100,100), size=(200,210)):
        self.ID = uuid.uuid4()

        self.POS = pos
        self.SIZE = size

        self.RECT = pg.Rect(self.POS[0], self.POS[1], self.SIZE[0], self.SIZE[1])
        self.COLOR = (0,0,0,255)

        self.ELEMENTS = []

    def new_rect(self):
        self.RECT = pg.Rect(self.POS[0], self.POS[1], self.SIZE[0], self.SIZE[1])

    def add_element(self, obj, relative_pos=(0,0)):
        obj.POS = (self.POS[0] + relative_pos[0], self.POS[1] + relative_pos[1])
        obj.new_rect()
        self.ELEMENTS.append(obj)

    def click(self, is_down, mouse_pos=(0,0)):
        obj = None
        for i in self.ELEMENTS:
            if i.RECT.collidepoint(mouse_pos[0], mouse_pos[1]):
                obj = i

        if obj:
            obj.click(is_down, mouse_pos)
        else:
            print("panel")

    def rclick(self, is_down, mouse_pos=(0,0)):
        print("rpanel")

    def draw(self):
        pg.draw.rect(WINDOW.SCREENUI, self.COLOR, self.RECT)
        for obj in self.ELEMENTS:
            obj.draw()

    def loop(self):
        self.draw()
