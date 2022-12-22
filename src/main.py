import pygame as pg
import sys
from settings import *
from map import *
from player import *
from object_renderer import *
from raycasting import *
from sprite import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.static_sprite = Sprite(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'Hill0x77 - DOOM: PSEUDO3d {self.clock.get_fps() :.1f}')

    def draw(self):
        # NOW WITH CEILING, DISABLE BLACK BACKGROUND
        # self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
