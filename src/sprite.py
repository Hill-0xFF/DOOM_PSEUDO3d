import pygame as pg
from settings import *

class Sprite:
    def __init__(self, game, path='src/resources/sprites/static/candlebra.png',
    pos=(10.5, 3.5), scale = 0.7, shift = 0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_HALF_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = shift

    def get_sprite_projection(self):
        projection = SCREEN_DISTANCE / self.norm_dist * self.SPRITE_SCALE
        projection_width, projection_height = projection * self.IMAGE_RATIO, projection

        image = pg.transform.scale(self.image, (projection_width, projection_height))
        self.sprite_half_width = projection_width // 2
        height_shift = projection_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - projection_height // 2 + height_shift

        self.game.raycasting.objects_torender.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta_angle = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta_angle += math.tau

        delta_rays = delta_angle / DELTA_ANGLE
        self.screen_x = (HALF_NUMRAYS + delta_rays) * SCALE
        
        self.dist = math.hypot(dx, dy)
        self.norm_dist =  self.dist * math.cos(delta_angle)
        if - self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()


    def update(self):
        self.get_sprite()