from .settings import *

FLOOR_WIDTH = 1020
FLOOR_HEIGHT = 180

class Home(pygame.sprite.Sprite):
    def __init__(self, n: int):
        pygame.sprite.Sprite.__init__(self)
        self.floors = []
        """
        for i in n:
            x = WIDTH/2
            y = HEIGHT - FLOOR_HEIGHT + FLOOR_HEIGHT/2
            floor = Floor(T)
            self.floors.append(floor)
        """

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
