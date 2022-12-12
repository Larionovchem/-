from .constants import SQUARE_SIZE, WOLF, SHEEP
import pygame

class Piece:
    """
    Задаёт доску и объекты на ней

        Атрибуты:
        ---------
        PADDING : int
            Создаёт двумерный список, содержащий данные о всех фишках
        OUTLINE : int
            Количество фишек овец
        row : int
            Строки
        col : int
            Столбцы
        color : int
            Условный цвет фишки
        x : int
            Координата по ОX
        y : int
            Координата по ОY

    """

    def __init__(self, row, col, color):
        """ Инициализация пакета"""
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """Вычисляет центр позиции фишки по столбцу (col) и строке (row)"""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2


    def draw(self, win):
        """Рисует фишки с иконками"""
        win.blit(WOLF, (self.x - WOLF.get_width() // 2, self.y - WOLF.get_height() // 2))
        win.blit(SHEEP, (self.x - WOLF.get_width() // 2, self.y - WOLF.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)