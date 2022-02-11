"""
animation module
"""

import pygame as pg

class Framelist:
    """List of frames of animation component"""
    def __init__(self, filename, count, rectangle):
        self.frames = []

        # LOAD FRAMES
        rect = pg.Rect(rectangle)
        spritesheet = pg.image.load(filename)
        for i in range(count):
            image = pg.Surface(rect.size, pg.SRCALPHA)
            image.blit(spritesheet, (0, 0), rect)
            rect.x = rect.x + rect.width
            self.frames.append(image)

class AnimationManager:
    """
    Manages all animations of one entity.
    To be declared in entity __init__.
    """
    def __init__(self, target_screen):
        """
        :param target_screen:  pg.Surface  surface where animation will be blitted
        ! don't forget to use change_animation() to start animation
        """
        self.animations = {}
        self.target_screen = target_screen
        self.is_flip = False

    def change_animation(self, name):
        self.current_frame = 0
        self.current_animation = name
        self.last_updated = pg.time.get_ticks()
        self.duration = self.animations[name+"_duration"]
        self.count = self.animations[name+"_count"]

    def add_animation(self, name, duration, count):
        """
        an animation is made of multiple components
        :param name:      string        name of the animation
        :param duration:  int           duration of one frame in ms
        :param count:     int           number of frames
        """
        self.animations[name] = []
        self.animations[name+"_duration"] = duration
        self.animations[name+"_count"] = count

    def add_animation_component(self, name, filename, rectangle):
        """
        component of an animation (ex: head, body, legs, sword)
        :param name:      string  name of parent animation
        :param filename:  string  filename of spritesheet
        :param rectangle: tuple   location/size on spritesheet ex: (0, 0*64, 64, 64)
        """
        self.animations[name].append(Framelist(filename, self.animations[name+"_count"], rectangle))

    def loop(self, position):
        """
        To be put in entity loop.
        :param position:  tuple  position on surface where animation takes place
        """
        if self.is_flip:
            for i in self.animations[self.current_animation]:
                self.target_screen.blit(pg.transform.flip(i.frames[self.current_frame], True, False), position)
        else:
            for i in self.animations[self.current_animation]:
                self.target_screen.blit(i.frames[self.current_frame], position)

        now = pg.time.get_ticks()
        if now - self.last_updated >= self.duration:
            self.current_frame = (self.current_frame + 1) % self.count
            self.last_updated = now
