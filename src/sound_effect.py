import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'src/resources/sound/'
        self.shotgun_sound = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.smg_sound = pg.mixer.Sound(self.path + 'smg.wav')
