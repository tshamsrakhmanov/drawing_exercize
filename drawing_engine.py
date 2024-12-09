import random

from colors import *
from drawing_functions import *
import pygame


def draw_window(pixel_matrix: PixelMatrix):
    def adjustable_triangle():

        radius = 15

        p1 = Point(50, 50)
        p2 = Point(250, 250)

        draw_circle(p1, radius, pixel_matrix, COLOR_RED)
        draw_circle(p2, radius, pixel_matrix, COLOR_RED)
        draw_line(p1, p2, pixel_matrix, COLOR_RED)

        if pygame.mouse.get_focused():
            p0 = Point(*pygame.mouse.get_pos())
            draw_circle(p0, radius, pixel_matrix, COLOR_WHITE)
            draw_line(p0, p1, pixel_matrix, COLOR_WHITE)
            draw_line(p0, p2, pixel_matrix, COLOR_WHITE)

    def random_lines():
        for _ in range(100):
            p0 = Point(random.randint(0, pixel_matrix.matrix_size_x), random.randint(0, pixel_matrix.matrix_size_y))
            p1 = Point(random.randint(0, pixel_matrix.matrix_size_x), random.randint(0, pixel_matrix.matrix_size_y))
            draw_line(p0, p1, pixel_matrix, COLOR_WHITE, True, COLOR_RANDOM(), COLOR_RANDOM())

    def random_circles():
        for _ in range(50):
            p0 = Point(random.randint(0, pixel_matrix.matrix_size_x), random.randint(0, pixel_matrix.matrix_size_y))
            draw_circle(p0, random.randint(10, 75), pixel_matrix, COLOR_RANDOM())

    # adjustable_triangle()
    # random_lines()
    random_circles()
