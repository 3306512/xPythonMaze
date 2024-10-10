from random import choice
from maze.maze import Moves
labyrinths = [
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
    ],
    [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ],
    [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ],
    [
        [1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
    ],
    [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
    ],

]


def generate_random_maze(height: int, width: int, sy: int, sx: int, endpoint: tuple) -> list[list]:
    """
    !!!!ВАЖНО!!!!
    Эта функция ВООБЩЕ не готова, ну вообще по сути свое задание выполняет, но функция не готова полностью,
    если её использовать будет видно, что это не особо похоже на лабиринт, а у меня всего по часу-два времени в день,
    когда могу свободно писать код. В общем тут есть список с лабиринтами, лучше юзать их.
    А эту Функцию я доделаю даже если вылечу с конкурса, самому интересно
    <3
    :param height: Высота лабиринта (Y)
    :param width: ширина лабиринта (X)
    :param sy: start-y - начальная координата Y
    :param sx: start-x - начальная координата X
    :param endpoint: кортеж с "координатами" выхода
    :return: list[list] - сгенерированный лабиринт
    """
    maze = []
    if (sx, sy) == endpoint:
        return maze
    for _ in range(height):
        maze.append([0 for _ in range(width)])
    maze[sy][sx] = 1
    goto = [Moves.UP, Moves.DOWN, Moves.RIGHT, Moves.LEFT]
    while (sx, sy) != endpoint:
        move = choice(goto)
        nx, ny = sx, sy
        if move == Moves.UP and sy > 0:
            sy -= 1
            ny = sy
            maze[ny][sx] = 1
        elif move == Moves.DOWN and sy < height - 1:
            sy += 1
            ny = sy
            maze[ny][sx] = 1
        elif move == Moves.RIGHT and sx < width - 1:
            sx += 1
            nx = sx
            maze[sy][nx] = 1
        elif move == Moves.LEFT and sx > 0:
            sx -= 1
            nx = sx
            maze[sy][nx] = 1
        if maze[ny][nx] == 0:
            sx, sy = nx, ny
            maze[sy][sx] = 1

    return maze
