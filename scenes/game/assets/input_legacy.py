"""docstring"""

import pygame as pg

class Input():
    def __init__(self, main):
        self.MAIN = main

        self.X, self.Y = pg.mouse.get_pos()
        self.XLAST, self.YLAST = self.X, self.Y

        self.EVENTS = None

        self.last_hover = None
        self.current_hover = None

        self.click_start_time = None
        self.clicked_obj = None
        self.drag_start_timer = 120
        self.drag_start_dist = 10
        self.is_drag = False
        
    def get_hover(self):
        obj = None
        for i in self.MAIN.cs().OBJECTS:
            if i.RECT.collidepoint(self.X // self.MAIN.WINDOW.SCALE, self.Y // self.MAIN.WINDOW.SCALE):
                obj = i
        for i in self.MAIN.cs().INTERFACE:
            if i.RECT.collidepoint(self.X, self.Y):
                obj = i
        return obj

    def hover_logic(self, obj):
        if obj != self.current_hover:
            self.last_hover = self.current_hover
            self.current_hover = obj

            if self.last_hover and hasattr(self.last_hover, "hover"):
                self.last_hover.hover(False)
            if self.current_hover and hasattr(self.current_hover, "hover"):
                self.current_hover.hover(True)

    def drag_logic(self):
        if not self.is_drag and self.click_start_time:
            if pg.time.get_ticks() - self.click_start_time > self.drag_start_timer or ((((self.X - self.XLAST )**2) + ((self.Y - self.YLAST)**2) )**0.5) > self.drag_start_dist:
                self.is_drag = True
                if hasattr(self.clicked_obj, "drag"):
                    self.clicked_obj.drag(True)

        if self.is_drag and hasattr(self.clicked_obj, "drag"):
            self.clicked_obj.add_pos(self.X - self.XLAST, self.Y - self.YLAST)

    def loop(self):
        self.XLAST, self.YLAST = self.X, self.Y
        self.X, self.Y = pg.mouse.get_pos()

        obj = self.get_hover()
        self.hover_logic(obj)

        for event in self.EVENTS:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: #LMB DOWN
                    if hasattr(obj, "click"):
                        obj.click(True)
                    self.click_start_time = pg.time.get_ticks()
                    self.clicked_obj = obj
                if event.button == 3: #RMB DOWN
                    if hasattr(obj, "rclick"):
                        obj.rclick(True)

            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1: #LMB UP
                    if not self.is_drag:
                        if hasattr(self.clicked_obj, "click"):
                            self.clicked_obj.click(False)
                    else:
                        if hasattr(self.clicked_obj, "drag"):
                            self.clicked_obj.drag(False)
                    self.is_drag = False
                    self.click_start_time = None
                    self.clicked_obj = None
                if event.button == 3: #RMB UP
                    if hasattr(obj, "rclick"):
                        obj.rclick(False)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.MAIN.cs().CAMERA.add_pos(0, -64)
                if event.key == pg.K_DOWN:
                    self.MAIN.cs().CAMERA.add_pos(0, 64)
                if event.key == pg.K_LEFT:
                    self.MAIN.cs().CAMERA.add_pos(-64, 0)
                if event.key == pg.K_RIGHT:
                    self.MAIN.cs().CAMERA.add_pos(64, 0)
                if event.key == pg.K_w:
                    self.MAIN.cs().OBJECTS[1].add_pos(0, -32)
                if event.key == pg.K_s:
                    self.MAIN.cs().OBJECTS[1].add_pos(0, 32)
                if event.key == pg.K_a:
                    self.MAIN.cs().OBJECTS[1].add_pos(-32, 0)
                if event.key == pg.K_d:
                    self.MAIN.cs().OBJECTS[1].add_pos(32, 0)

        self.drag_logic()
