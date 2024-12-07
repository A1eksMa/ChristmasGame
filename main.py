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

floor_1 = Floor(BLUE, (WIDTH-FLOOR_WIDTH)/2, FLOOR_HEIGHT*1)
floor_2 = Floor(GRAY, (WIDTH-FLOOR_WIDTH)/2, FLOOR_HEIGHT*2)
floor_3 = Floor(BLUE, (WIDTH-FLOOR_WIDTH)/2, FLOOR_HEIGHT*3)
home.add(floor_1)
home.add(floor_2)
home.add(floor_3)

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
    screen.fill(BLACK)
    home.draw(screen)
    sprites.draw(screen)

    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
