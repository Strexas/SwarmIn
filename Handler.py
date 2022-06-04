import pygame as pg


class Handler:
    def hand(self, world):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                world.live = False
