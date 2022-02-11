import pygame as pg
from window import WINDOW

#Define Colours
COLOR_DICT = {
    "WHITE": (255,255,255),
    "GREEN": (0,255,0),
    "RED": (255,0,0),
    "BLUE": (0,0,255),
    "BLACK": (0,0,0),
    "FUCHSIA": (255, 0, 255),
    "GRAY": (128, 128, 128),
    "LIME": (0, 128, 0),
    "MAROON": (128, 0, 0),
    "NAVYBLUE": (0, 0, 128),
    "OLIVE": (128, 128, 0),
    "PURPLE": (128, 0, 128),
    "TEAL": (0,128,128)
}

class AdvancedText:
    def __init__(self, pos, text, max_width=1000, text_size=32, text_color="WHITE"):
        self.POS = pos
        self.TEXT = text
        self.MAX_WIDTH = max_width
        self.TEXT_SIZE = text_size
        self.TEXT_ARRAY = []
        self.TEXT_COLOR = COLOR_DICT[text_color]
        self.TEXT_COLOR_CURRENT = COLOR_DICT[text_color]

        self.RECT = pg.Rect(self.POS[0],self.POS[1],0,0)
        self.FONT = pg.font.Font('m5x7.ttf', self.TEXT_SIZE)
        
        self.RENDER = pg.Surface((1000,300), pg.SRCALPHA)
        self.render()

    def render(self):
        #SPLIT INTO LINES
        line = ""
        line_full = ""
        for i in self.TEXT.split(" "):
            if i == "#P":
                self.TEXT_ARRAY.append(line_full)
                line = ""
                line_full = ""                
            elif len(i) > 0 and i[0] == "#":
                line_full = line_full + i + " "
            else:
                line = line + i + " "
                line_full = line_full + i + " "

                render = self.FONT.render(line, False, self.TEXT_COLOR)
                if render.get_rect().width > self.MAX_WIDTH:
                    line = line[:-len(i)-1]
                    line_full = line_full[:-len(i)-1]
                    self.TEXT_ARRAY.append(line_full)
                    line = i + " "
                    line_full = i + " "
        self.TEXT_ARRAY.append(line_full)

        #RENDER ACCORDING TO TAGS
        offset = [0, 0]
        line = ""
        for i in self.TEXT_ARRAY:
            for j in i.split(" "):
                if len(j)>0 and j[0] == "#":
                    font_text = self.FONT.render(line, False, self.TEXT_COLOR_CURRENT)
                    text_rect = font_text.get_rect()
                    text_rect.x = offset[0]
                    text_rect.y = offset[1]
                    self.RENDER.blit(font_text, text_rect)
                    if j == "#ORIGINAL":
                        self.TEXT_COLOR_CURRENT = self.TEXT_COLOR
                    else:
                        self.TEXT_COLOR_CURRENT = COLOR_DICT[j[1:]]             
                    offset[0] += text_rect.width
                    line = ""
                else:
                    line = line + j + " "
            font_text = self.FONT.render(line, False, self.TEXT_COLOR_CURRENT)
            text_rect = font_text.get_rect()
            text_rect.x = offset[0]
            text_rect.y = offset[1]
            self.RENDER.blit(font_text, text_rect)
            offset = [0, offset[1]+text_rect.height]
            line = ""
        self.TEXT_COLOR_CURRENT = self.TEXT_COLOR

    def draw(self):
        WINDOW.SCREENUI.blit(self.RENDER, self.POS)

    def loop(self):
        self.draw()
