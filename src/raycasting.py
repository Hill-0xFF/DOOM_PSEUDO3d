import pygame as pg
# from player import *
from settings import *
import math

class Raycasting:
    def __init__(self, game):
        self.game = game

    def raycast(self):
        pos_x, pos_y = self.game.player.pos
        tilePosX_map, tilePosY_map = self.game.player.map_pos
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range (NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # VERTICAL
            x_vert, dx = (tilePosX_map + 1, 1) if cos_a > 0 else (tilePosX_map - 1e-6, -1)
            depth_vert = (x_vert - pos_x) / cos_a
            y_vert = pos_y + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
            
            # HORIZONTAL
            y_hor, dy = (tilePosY_map + 1, 1) if sin_a > 0 else (tilePosY_map - 1e-6, -1)
            depth_hor = (y_hor - pos_y) / sin_a
            x_hor = pos_x + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth
            
            # determing the DEPTH
            if depth_vert < depth_hor:
                depth = depth_vert
            else: 
                depth = depth_hor

            # Casting the rays
            # pg.draw.line(self.game.screen, 'white', (100 * pos_x, 100 * pos_y),
            # (100 * pos_x + 100 * depth * cos_a, 100 * pos_y + 100 * depth * sin_a), 2)
            
            # REMOVING EYEFISH EFFECT
            depth *= math.cos(self.game.player.angle - ray_angle)

            # PROJECTION HEIGHT
            projection_height = SCREEN_DISTANCE / (depth + 0.0001)
            
            # SHOW WALLS
            color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen, color,
            (ray * SCALE, HALF_HEIGHT - projection_height // 2, SCALE, projection_height))
            ray_angle += DELTA_ANGLE

    def update(self):
        self.raycast()
