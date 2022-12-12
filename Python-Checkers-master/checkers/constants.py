import pygame

# Размеры окна
WIDTH, HEIGHT = 600, 600

# Количество строк и столбцов
ROWS, COLS = 8, 8

# Размер клетки игрового поля
SQUARE_SIZE = WIDTH // COLS

# Цвета
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (128, 255, 128)

# Изображения
WOLF = pygame.transform.scale(pygame.image.load('Wolf.png'), (80, 80))
SHEEP = pygame.transform.scale(pygame.image.load('Sheep.png'), (80, 80))
MENU_BACKGROUND = pygame.transform.scale(pygame.image.load('Logo_klovn.png'), (WIDTH, HEIGHT))
pass
