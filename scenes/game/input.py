"""basic input"""

import pygame as pg

from window import WINDOW
from scenes.game.camera import CAMERA
from scenes.game.templates_instances import CHARACTER0
from scenes.game.grid import GRID

# TODO CREATE HOVER, CREATE DRAG

class Input():
    def __init__(self):
        self.POS_LAST = None
        self.POS = pg.mouse.get_pos()

    def loop(self, objects, interface):
        self.POS_LAST = self.POS
        self.POS = pg.mouse.get_pos()
        is_interface = False

        obj = None
        for i in objects:
            if i.RECTSCREEN.collidepoint(self.POS[0]//WINDOW.SCALE, self.POS[1]//WINDOW.SCALE):
                obj = i  
        for i in interface:
            if i.RECT.collidepoint(self.POS[0], self.POS[1]):
                obj = i
                is_interface = True

        for event in WINDOW.EVENTS:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: #LMB DOWN
                    if obj:
                        if is_interface:
                            obj.click(True, (self.POS[0], self.POS[1]))
                        else:
                            obj.click(True, (self.POS[0]//WINDOW.SCALE, self.POS[1]//WINDOW.SCALE))
                    else:
                        pass
                if event.button == 3: #RMB DOWN
                    if obj:
                        if is_interface:
                            obj.rclick(True, (self.POS[0], self.POS[1]))
                        else:
                            obj.rclick(True, (self.POS[0]//WINDOW.SCALE, self.POS[1]//WINDOW.SCALE))
                    else:
                        CHARACTER0.move_to_point_pathfinding((self.POS[0]//WINDOW.SCALE+CAMERA.POS[0], self.POS[1]//WINDOW.SCALE+CAMERA.POS[1]))

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1: #LMB UP
                    if obj:
                        if is_interface:
                            obj.click(False, (self.POS[0], self.POS[1]))
                        else:
                            obj.click(False, (self.POS[0]//WINDOW.SCALE, self.POS[1]//WINDOW.SCALE))
                    else:
                        pass
                if event.button == 3: #LMB UP
                    if obj:
                        if is_interface:
                            obj.rclick(False, (self.POS[0], self.POS[1]))
                        else:
                            obj.rclick(False, (self.POS[0]//WINDOW.SCALE, self.POS[1]//WINDOW.SCALE))
                    else:
                        pass

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    CAMERA.add_pos((0, -32), objects)
                if event.key == pg.K_DOWN:
                    CAMERA.add_pos((0, 32), objects)
                if event.key == pg.K_LEFT:
                    CAMERA.add_pos((-32, 0), objects)
                if event.key == pg.K_RIGHT:
                    CAMERA.add_pos((32, 0), objects)
                if event.key == pg.K_w:
                    pass
                if event.key == pg.K_s:
                    pass
                if event.key == pg.K_a:
                    pass
                if event.key == pg.K_d:
                    pass
                if event.key == pg.K_1:
                    CHARACTER0.SM.change_state("attackWeapon3")
                if event.key == pg.K_2:
                    pass

            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    pass
                if event.key == pg.K_s:
                    pass
                if event.key == pg.K_a:
                    pass
                if event.key == pg.K_d:
                    pass

INPUT = Input()
