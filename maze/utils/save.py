import cv2
import numpy


def save_maze(maze: list[list], o_file: str) -> bool:
    """
       Функция сохраняет лабиринт в виде фото
       :param maze: лабиринт
       :param o_file: имя файла куда сохраняется фото лабиринта
       :return:
       """
    try:
        im = numpy.array(maze)
        cv2.imwrite(o_file, im * 255.0)
        return True
    except cv2.error:
        return False
