from src.settings import *
from src.Santa import *
from src.Home import *

# создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
home = pygame.sprite.Group()

for floor in Home(3).floors:
    home.add(floor)
    for room in floor.rooms:
        home.add(room)

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
    home.update()
    sprites.update()

    # Рендеринг
    screen.fill(Colors.BLACK.value)
    home.draw(screen)
    sprites.draw(screen)

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
