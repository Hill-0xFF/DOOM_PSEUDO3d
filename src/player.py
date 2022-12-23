import pygame as pg
import math
from settings import *

PLAYER_POS = 1.5, 5 
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shotsfired = False

    def shot_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shotsfired and not self.game.weapons.reloading:
                self.shotsfired = True
                self.game.weapons.reloading = True


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        self.shotsfired = False

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


        # DISABLED LEFT AND RIGHT ARROW KEYS
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        self.angle %= math.tau

    def hit_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def collision_detection_wall(self , dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.hit_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.hit_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
    
    # def draw(self):
        # pg.draw.line(self.game.screen, 'red', (self.x * 20, self.y * 20),
        # (self.x * 20 + WIDTH * math.cos(self.angle),
        # self.y * 20 + WIDTH * math.sin(self.angle)), 2)
        
        # pg.draw.circle(self.game.screen, 'green', (self.x * 20, self.y * 20), 5)

    def mouse_control(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x < MOUSE_BORDER_LEFT or mouse_x > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.relative = pg.mouse.get_rel()[0]
        self.relative = max(-MOUSE_RELATIVE_MOVEMENT, min(MOUSE_RELATIVE_MOVEMENT, self.relative))
        self.angle += self.relative * MOUSE_SENSITIVITY * self.game.delta_time

        # SOME ATTEMPTS TO GIVE A FEEL OF HEADS UP AND DOWN
        if mouse_y > MOUSE_BORDER_DOWN or mouse_y < MOUSE_BORDER_UP:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.relative = pg.mouse.get_rel()[0]
        # self.relative = min(MOUSE_RELATIVE_MOVEMENT, max(MOUSE_RELATIVE_MOVEMENT, self.relative))
        self.angle += self.relative * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    