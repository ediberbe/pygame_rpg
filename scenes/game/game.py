"""game scene"""

import pygame as pg
from window import WINDOW

from scenes.game.camera import CAMERA
from scenes.game.input import INPUT
from scenes.game.map import MAP
from scenes.game.grid import GRID

from scenes.game.templates_instances import *
from scenes.game.advanced_text import AdvancedText
from scenes.game.universal_button import UniversalButton

class Game:
    def __init__(self):
        # TODO add self.ENGINE = []
        self.OBJECTS = []
        self.INTERFACE = []

    def add_object(self, obj):
        self.OBJECTS.append(obj)

    def add_interface(self, obj):
        self.INTERFACE.append(obj)

    def loop(self):
        WINDOW.SCREEN.fill((0, 100, 0))
        WINDOW.SCREENUI.fill((0, 0, 0, 0))

        for event in WINDOW.EVENTS:
            if event.type == pg.QUIT:
                WINDOW.LOOP = False

        # TODO add self.ENGINE = [], for obj in self.ENGINE:
        MAP.loop(CAMERA.POS)
        CAMERA.loop(GRID.GRID)
        INPUT.loop(self.OBJECTS, self.INTERFACE)
        GRID.loop()

        for obj in self.OBJECTS:
            obj.loop()
        for obj in self.INTERFACE:
            obj.loop()

GAME = Game()
GAME.add_object(CHARACTER0)
GAME.add_object(Fence(2,6))
GAME.add_object(Fence(2,7))
GAME.add_object(Fence(2,8))
GAME.add_object(Fence(2,9))
GAME.add_object(Fence(3,6))
GAME.add_object(Fence(4,6))
GAME.add_object(Fence(5,6))
GAME.add_object(Fence(6,6))
GAME.add_object(Fence(6,7))
GAME.add_object(Fence(6,8))
GAME.add_object(Fence(6,9))
GAME.add_object(Fence(5,9))

TEXT = AdvancedText((400,400), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque tortor quis enim sodales aliquet. Phasellus rhoncus purus ut nisi tincidunt, nec lobortis neque dictum. Ut eu leo vitae diam sollicitudin bibendum ut et metus. Maecenas at dolor aliquet, molestie urna quis, efficitur magna. Integer ut lacinia eros. Quisque porta maximus arcu. #P Vivamus vulputate velit justo, eu #GREEN condimentum #ORIGINAL dolor tincidunt quis. ")
GAME.add_interface(TEXT)

CONTEXTMENU = ContextMenu()
CONTEXTMENU.add_element(UniversalButton((0,0), (200,60), "buna", print, "buna", "dimineata", rect_color=(255,0,0)))
CONTEXTMENU.add_element(UniversalButton((0,0), (200,60), "hello", print, "good", "morning", rect_color=(0,255,0)))
GAME.add_interface(CONTEXTMENU)
