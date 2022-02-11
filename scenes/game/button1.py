import pygame as pg
import uuid

from window import WINDOW

# TODO CREATE TEMPLATE, CREATE UI PANEL

class Button1():
    def __init__(self):
        self.ID = uuid.uuid4()
        self.X = 1700
        self.Y = 1000
        self.WIDTH = 200
        self.HEIGHT = 60

        self.TEXT = "Hello"
        self.TEXT_SIZE = 32
        self.TEXT_COLOR = (255,255,255)

        self.RECT = pg.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        self.RECT_COLOR = (0,0,0)

        self.FONT = pg.font.Font('m5x7.ttf', self.TEXT_SIZE)
        self.FONT_TEXT = self.FONT.render(self.TEXT, False, self.TEXT_COLOR)
        self.TEXT_RECT = self.FONT_TEXT.get_rect()
        self.TEXT_RECT.center = (self.RECT.x + self.RECT.width // 2), (self.RECT.y + self.RECT.height // 2)

    def change_pos(self, x, y):
        self.X = x
        self.Y = y
        self.RECT = pg.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)

    def add_pos(self, x, y):
        self.X += x
        self.Y += y
        self.RECT = pg.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)

    def click(self, is_down, mouse_pos):
        if is_down:
            print("button1 LMB DOWN")
        else:
            print("button1 LMB UP")

    def rclick(self, is_down, mouse_pos):
        if is_down:
            print("button1 RMB DOWN")
        else:
            print("button1 RMB UP")

    def draw(self):
        self.RECT = pg.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        self.TEXT_RECT.center = (self.RECT.x + self.RECT.width // 2), (self.RECT.y + self.RECT.height // 2)
        pg.draw.rect(WINDOW.SCREENUI, self.RECT_COLOR, self.RECT)
        WINDOW.SCREENUI.blit(self.FONT_TEXT, self.TEXT_RECT)

    def loop(self):
        self.draw()

BUTTON1 = Button1()
