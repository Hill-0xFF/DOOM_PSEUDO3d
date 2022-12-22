import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.ceiling = self.get_texture('src/resources/textures/moon.png', (WIDTH, HALF_HEIGHT))
        self.ceiling_offset = 0

    def draw(self):
        self.draw_ceil()
        self.render_game_objects()

    def draw_ceil(self):
        self.ceiling_offset = (self.ceiling_offset + 4.5 * self.game.player.relative) % WIDTH
        self.screen.blit(self.ceiling, (-self.ceiling_offset, 0))
        self.screen.blit(self.ceiling, (-self.ceiling_offset + WIDTH, 0))
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_torender
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

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