from .settings import *

#img = pygame.image.load(os.path.join(img_folder, 'alien.png')).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, floor):
        pygame.sprite.Sprite.__init__(self)
        self.floor = floor
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x #(WIDTH-FLOOR_WIDTH)/2
        self.rect.y = self.floor.y + 2 * 60 #4*FLOOR_HEIGHT - 60
        self.speedy = 0
        self.speedx = 0
        self.step = 6

    def update(self):
        self.speedy = 0
        self.speedx = 0

        keystate = pygame.key.get_pressed()
        """
        if keystate[pygame.K_UP]:
            self.speedy = -self.step
        if keystate[pygame.K_DOWN]:
            self.speedy = self.step
        """
        if keystate[pygame.K_LEFT] and self.rect.x > self.floor.left_edge:
            self.speedx = -self.step
        if keystate[pygame.K_RIGHT] and self.rect.x + 60 < self.floor.right_edge:
            self.speedx = self.step

        self.rect.y += self.speedy
        self.rect.x += self.speedx

class Santa(Player):
    pass
