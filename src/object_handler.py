from sprite import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'src/resources/sprites'
        self.animated_sprites = 'src/resources/sprites/animated/'

    # Sprite Map
        self.addSprite(Sprite(game))
        self.addSprite(AnimatedSprite(game))
        self.addSprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        self.addSprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        self.addSprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        self.addSprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        self.addSprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        self.addSprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        self.addSprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        self.addSprite(AnimatedSprite(game,
        path = self.animated_sprites + 'redlight/0.png', pos=(14.5, 8.5)))
        self.addSprite(AnimatedSprite(game,
        path = self.animated_sprites + 'redlight/0.png', pos=(11, 8.5)))
        self.addSprite(AnimatedSprite(game, 
        path = self.animated_sprites + 'redlight/0.png', pos=(8.5, 8.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def addSprite(self, sprite):
        self.sprite_list.append(sprite)

    # addSprite(Sprite(game))
    # addSprite(AnimatedSprite(game))