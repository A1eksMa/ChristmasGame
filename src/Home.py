from .settings import *
import random

FLOOR_WIDTH = 1020
FLOOR_HEIGHT = 180

class Home(pygame.sprite.Sprite):
    def __init__(self, n: int):
        pygame.sprite.Sprite.__init__(self)
        self.floors = []
        for i in range(n):
            color = random.choice(colors)
            x = (WIDTH-FLOOR_WIDTH)/2
            y = FLOOR_HEIGHT*(i+1)
            self.floors.append(Floor(color, x, y))

class Floor(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((FLOOR_WIDTH, FLOOR_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Room:
    pass

class Stairway:
    pass
