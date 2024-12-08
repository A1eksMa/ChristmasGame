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


class Home:
    def __init__(self, x, y):
        # Координаты левого верхнего угла дома
        self.x = x
        self.y = y
        # этажи
        self.floors = []

    def add_floor(self):
        floor = Floor(self.x, self.y + (FLOOR_HEIGHT) * (len(self.floors)))
        self.floors.append(floor)

    def __repr__ (self):
        return f"Home: x {self.x}, y {self.y}, floors cnt {len(self.floors)}"


class Floor():
    def __init__(self, x, y):
        # Координаты левого верхнего угла этажа
        self.x = x
        self.y = y
        # Комнаты
        self.rooms = []

    def add_room(self, l):
        room = Room(self.x + sum([room.l for room in self.rooms]), self.y, l)
        self.rooms.append(room)

    def __repr__ (self):
        return f"Floor: x {self.x}, y {self.y}, rooms cnt {len(self.rooms)}"


class Room(pygame.sprite.Sprite):
    def __init__(self, x, y, l):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((l, FLOOR_HEIGHT))
        self.image.fill(random.choice(colors))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Координаты левого верхнего угла этажа
        self.x = x
        self.y = y
        # Длина комнаты
        self.l = l

    def __repr__ (self):
        return f"Room: x {self.x}, y {self.y}, length {self.l}"


class Stairway:
    pass
