"""
movement module
"""

import pygame as pg
import math

class MovementManager():
    """
    Manages all movement of one entity.
    To be declared in entity __init__.
    ! Don't forget to link with entity pos.
    """
    def __init__(self, position, speed, friction):
        """
        :param position:  tuple (x,y)  starting position of entity
        :param speed:     int x        how fast the entity moves
        :param friction:  float x      subunitary, Higher -> Slippery
        """
        self.position = position
        self.positionspx = [self.position[0]*100, self.position[1]*100]

        self.speed = speed
        self.direction = [0, 0]
        self.angle = 0

        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.friction = friction

    def up(self):
        """
        Moves entity up.
        """
        self.direction[1] += 1

    def down(self):
        """
        Moves entity down.
        """
        self.direction[1] -= 1

    def left(self):
        """
        Moves entity left.
        """
        self.direction[0] -= 1
        
    def right(self):
        """
        Moves entity right.
        """
        self.direction[0] += 1

    def loop(self):
        """
        To be put in entity loop.
        """
        vec = pg.Vector2(self.direction)
        
        # DIRECTION VECTOR
        vec = pg.math.Vector2.rotate(vec, self.angle)
        if pg.math.Vector2.length(vec) != 0:
            pg.math.Vector2.scale_to_length(vec, self.speed)
        self.acceleration[0] = vec[0]
        self.acceleration[1] = -vec[1]

        # PHYSICS
        self.velocity = [x + y for x, y in zip(self.velocity, self.acceleration)]
        self.velocity = [element * self.friction for element in self.velocity]
        self.positionspx = [x + y for x, y in zip(self.positionspx, self.velocity)]
        self.position = [math.floor(element / 100) for element in self.positionspx]
