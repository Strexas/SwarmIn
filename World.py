import pygame as pg
from Drawer import Drawer
from Handler import Handler
from consts import size


class World:
    def __init__(self):
        self.live = True
        self.drawer = Drawer()
        self.handler = Handler()
        self.clock = pg.time.Clock()
        self.world = pg.display.set_mode(size)

    def tick(self):
        self.clock.tick(120)
        self.drawer.draw(self)
        self.handler.hand(self)
