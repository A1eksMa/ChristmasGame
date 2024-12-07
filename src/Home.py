from .settings import *
import random

class Room_size(Enum):
    x1 = 60*4
    x2 = 60*5
    x3 = 60*6
    x4 = 60*7
    x5 = 60*8
    x6 = 60*9
    x7 = 60*10

room_sizes = [x.value for x in Room_size]

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
        self.rooms = []

        # generate_rooms
        """
        l = 0
        lenghts = []
        while l != FLOOR_WIDTH:
            l_random = random.choice(room_sizes)
            if FLOOR_WIDTH - (l + l_random) < Room_size.x1.value:
                continue
            else:
                lenghts.append(l_random)
                l+=l_random

        """
        lenghts = [540,540]
        l = self.rect.x

        for lenght in lenghts:
            self.rooms.append(Room(random.choice(colors),
                                   l,
                                   self.rect.y,
                                   lenght)
                             )
            l+=lenght

class Room(pygame.sprite.Sprite):
    def __init__(self, color, x, y, l):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((l, FLOOR_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Stairway:
    pass
