import random
from maze.maze import Maze
from maze.utils.save import save_maze
from maze.utils.generation import labyrinths


def main():
    endpoint = (4, 4)
    startpoint = (0, 0)

    maze_for_class = random.choice(labyrinths)
    maze = Maze(maze_for_class)
    if not save_maze(maze_for_class, 'maze.png'):
        print("Error, can't save file")

    if maze.solve_maze(*startpoint, endpoint=endpoint):
        print('Solved!')
    else:
        print('Failed!')


if __name__ == '__main__':
    main()
