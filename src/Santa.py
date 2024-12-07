from .settings import *

#img = pygame.image.load(os.path.join(img_folder, 'alien.png')).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(Colors.RED.value)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH-FLOOR_WIDTH)/2
        self.rect.y = 4*FLOOR_HEIGHT - 60
        self.speedy = 0
        self.speedx = 0
        self.step = 6

    def update(self):
        self.speedy = 0
        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -self.step
        if keystate[pygame.K_DOWN]:
            self.speedy = self.step
        if keystate[pygame.K_LEFT]:
            self.speedx = -self.step
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.step

        self.rect.y += self.speedy
        self.rect.x += self.speedx

class Santa(Player):
    pass
