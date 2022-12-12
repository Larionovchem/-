import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, MENU_BACKGROUND
from checkers.game import Game
from sys import exit

pygame.init()

FPS = 60

# Отрисовка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Название игры
pygame.display.set_caption('Волки и овца')

# Музыка
alpha_shtrih = pygame.mixer.music.load('alpha_shtrih.mp3')
pygame.mixer.music.play(-1)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def menu(start):
    """Создание меню"""
    pygame.init()

    while start:

        # Фон
        pygame.display.update()
        screen.blit(MENU_BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos1, pos2 = pygame.mouse.get_pos()

                # Кнопка для старта
                if (pos1 - WIDTH//2) ** 2 + (pos2 - HEIGHT//2) ** 2 <= (WIDTH * 0.096) ** 2:
                    main(True)
                    start = False

    pygame.quit()
    exit()

def main(run):
    """Цикл игры"""
    pygame.init()
    clock = pygame.time.Clock()
    game = Game(screen)

    while run:
        clock.tick(FPS)

        # Завершение игры при определении победителя раунда
        '''if game.winner() != None:
            print(game.winner())
            run = False'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()
    exit()


menu(True)

main(True)