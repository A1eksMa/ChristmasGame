import pygame
import os
from enum import Enum


# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

WIDTH = 1200  # ширина игрового окна
HEIGHT = 780 # высота игрового окна
FPS = 60 # частота кадров в секунду


class Colors(Enum):
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

colors = list(Colors.__members__.values())
