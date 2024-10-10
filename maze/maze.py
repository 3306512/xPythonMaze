from random import choice
from enum import Enum


class Moves(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Maze:
    """
    Сделал класс т.к очень удобно использовать метод
    """
    def __init__(self, grid: list[list]):
        """
        :param grid: матрица (2д массив) с числами 0 для стен и 1 для свободного пути
        """
        self.grid = grid

    def solve_maze(self, sx: int, sy: int, endpoint: tuple) -> bool:
        """
        Метод для прохождения лабиринта
        :param sx:
        :param sy:
        :param endpoint: кортеж с "координатами" выхода,
               чисто теоретически я бы мог сделать выход другим символом,
               но это не меняло бы многого
        :return: bool: True - если удалось пройти лабиринт; False - выход не найден
        """
        self.grid[sy][sx] = 0.5
        if (sx, sy) == endpoint:
            return True

        goto = [Moves.UP, Moves.DOWN, Moves.RIGHT, Moves.LEFT]
        while goto:
            move = choice(goto)
            goto.remove(move)

            nx, ny = sx, sy
            if move == Moves.UP and sy > 0:
                ny = sy - 1
            elif move == Moves.DOWN and sy < len(self.grid) - 1:
                ny = sy + 1
            elif move == Moves.RIGHT and sx < len(self.grid[0]) - 1:
                nx = sx + 1
            elif move == Moves.LEFT and sx > 0:
                nx = sx - 1

            if self.grid[ny][nx] == 1:
                if self.solve_maze(nx, ny, endpoint):
                    return True

        return False
