import uuid
import pygame as pg
from window import WINDOW

class UniversalButton:
    def __init__(self, pos=(0,0), size=(200,60), text="hello", func=print, *args, rect_color=(0,0,0,255),text_size=32, text_color=(255,255,255), font="m5x7.ttf"):
        self.ID = uuid.uuid4()

        self.POS = pos
        self.SIZE = size

        self.RECT = pg.Rect(self.POS[0], self.POS[1], self.SIZE[0], self.SIZE[1])
        self.RECT_COLOR = rect_color

        self.FUNC = func
        self.ARGS = args

        self.TEXT = text
        self.TEXT_SIZE = text_size
        self.TEXT_COLOR = text_color
        self.FONT = pg.font.Font(font, self.TEXT_SIZE)
        self.FONT_TEXT = self.FONT.render(self.TEXT, False, self.TEXT_COLOR)
        self.TEXT_RECT = self.FONT_TEXT.get_rect()
        self.TEXT_RECT.center = (self.RECT.x + self.RECT.width // 2), (self.RECT.y + self.RECT.height // 2)

    def new_rect(self):
        self.RECT = pg.Rect(self.POS[0], self.POS[1], self.SIZE[0], self.SIZE[1])
        self.TEXT_RECT.center = (self.RECT.x + self.RECT.width // 2), (self.RECT.y + self.RECT.height // 2)

    def click(self, is_down, mouse_pos):
        if is_down:
            self.FUNC(*self.ARGS)

    def rclick(self, is_down, mouse_pos):
        pass

    def draw(self):
        pg.draw.rect(WINDOW.SCREENUI, self.RECT_COLOR, self.RECT)
        WINDOW.SCREENUI.blit(self.FONT_TEXT, self.TEXT_RECT)

    def loop(self):
        self.draw()
