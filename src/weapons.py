from sprite import * 

# class Weapons(AnimatedSprite):
#     def __init__(self, game, path='src/resources/sprites/weapons/shotgun/0.png',
#     scale=0.4, animation_time=90):

#         super().__init__(game = game, path = path, scale = scale, animation_time = animation_time)
#         self.images = deque(
#             [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
#             for img in self.images])

#         self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())

#     def draw(self):
#         self.game.screen.blit(self.images[0], self.weapon_pos)

#     def update(self):
#         pass
class Weapons(AnimatedSprite):
    def __init__(self, game, path = 'src/resources/sprites/weapons/shotgun/1.png', scale = 0.4, animation_time = 120):
        super().__init__(game = game, path = path, scale = scale, animation_time = animation_time)

        # self.image = pg.image.load(path).convert_alpha()
        # self.path = path.rsplit('/', 1)[0]
        # self.image = self.get_images(self.path)
        # print(type(self.images))

        # For reasons not yet known, I cannot figure out why it's not showing the correct shotgun sprite
        # So, it's gonna be the path arg provided above that seems to 'fix', temporarily, the sprite.

        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
            for img in self.images]
            )
        # print(self.images[0])
        # print(self.images[1])
        # print(self.images[2])
        # print(self.images[3])
        # print(self.images[4])
        # print(self.images[5])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)
        # pass

    def update(self):
        self.check_animation_time()
        self.animate_shot()