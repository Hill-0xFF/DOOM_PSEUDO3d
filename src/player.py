import pygame as pg
import math
from settings import *

PLAYER_POS = 1.5, 5 
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos

        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # update player coordinates
        # self.x += dx
        # self.y += dy
        
        self.collision_detection_wall(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        self.angle %= math.tau

    def hit_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def collision_detection_wall(self , dx, dy):
        if self.hit_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.hit_wall(int(self.x), int(self.y + dy)):
            self.y += dy
    
    # def draw(self):
        # pg.draw.line(self.game.screen, 'red', (self.x * 20, self.y * 20),
        # (self.x * 20 + WIDTH * math.cos(self.angle),
        # self.y * 20 + WIDTH * math.sin(self.angle)), 2)
        
        # pg.draw.circle(self.game.screen, 'green', (self.x * 20, self.y * 20), 5)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    