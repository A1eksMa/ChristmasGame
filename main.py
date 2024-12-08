from src.settings import *
from src.Santa import *
from src.Home import *

# создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()

home = Home(30,180)
home.add_floor()
home.add_floor()
home.add_floor()
home.floors[0].add_room(180)
home.floors[0].add_room(360)
home.floors[0].add_room(600)
home.floors[1].add_room(600)
home.floors[1].add_room(180)
home.floors[1].add_room(360)
home.floors[2].add_room(300)
home.floors[2].add_room(300)
#home.floors[2].add_room(540)

for floor in home.floors:
    for room in floor.rooms:
        sprites.add(room)


santa = Santa()
sprites.add(santa)

# Цикл игры
run = True
while run:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            run = False

    # Обновление
    sprites.update()

    # Рендеринг
    screen.fill((0, 0, 0))
    sprites.draw(screen)

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
