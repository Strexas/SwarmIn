from pygame import quit
from World import World

game = World()

while game.live:
    game.tick()

quit()
