import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('src/resources/textures/001.png'),
            2: self.get_texture('src/resources/textures/002.png'),
            3: self.get_texture('src/resources/textures/003.png'),
            4: self.get_texture('src/resources/textures/004.png'),
            5: self.get_texture('src/resources/textures/005.png'),
        }