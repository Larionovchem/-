import pygame
from .constants import BLACK, ROWS, SQUARE_SIZE, COLS, WHITE
from .piece import Piece


class Board:
    """
    Задаёт доску и объекты на ней

        Атрибуты:
        ---------
        board : list
            Создаёт двумерный список, содержащий данные о всех фишках
        sheep : int
            Количество фишек овец
        wolf : int
            Количество фишек волков
        sheep_winner : bool
            Победили ли овцы
        wolf_winner : bool
            Победили ли волки

    """
    def __init__(self):
        """ Инициализация пакета"""
        self.board = []
        self.sheep = 1
        self.wolf = 4
        self.sheep_winner = False
        self.wolf_winner = False
        self.create_board()

    def draw_squares(self, win):
        """Задаёт отрисовку клеток игрового поля в выбранном окне"""
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == RED:
                self.winner_sheep = True

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        """Вносит данные но фишках на игровом поле"""
        for row in range(ROWS):
            # Создаёт нового списка для новой строки
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 1:
                        # Вносит данные о фишках волков
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 6 and col == 4:
                        # Вносит данные о фишках овец
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        """Рисует клетки игрового поля в местах, где фишки отсутствуют"""
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def winner(self):
        if sheep_winner:
            return print(1)
        elif wolf_winner:
            return print(0)
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == WHITE:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == BLACK or WHITE:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
