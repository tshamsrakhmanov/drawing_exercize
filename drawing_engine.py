import random

from colors import *
from drawing_functions import *
import pygame


def draw_window(pixel_array: pygame.pixelarray):
    def adjustable_triangle():

        radius = 15

        p1 = Point(50, 50)
        p2 = Point(250, 250)
        p3 = Point(350, 100)

        draw_circle(p1, radius, pixel_array, COLOR_RED)
        draw_circle(p2, radius, pixel_array, COLOR_RED)
        draw_circle(p3, radius, pixel_array, COLOR_RED)
        draw_line(p1, p2, pixel_array, COLOR_RED)
        draw_line(p2, p3, pixel_array, COLOR_RED)
        draw_line(p1, p3, pixel_array, COLOR_RED)

        if pygame.mouse.get_focused():
            p0 = Point(*pygame.mouse.get_pos())
            draw_circle(p0, radius, pixel_array, COLOR_WHITE)
            draw_line(p0, p1, pixel_array, COLOR_WHITE)
            draw_line(p0, p2, pixel_array, COLOR_WHITE)
            draw_line(p0, p3, pixel_array, COLOR_WHITE)

    def random_lines():
        for _ in range(500):
            p0 = Point(random.randint(10, pixel_array.surface.get_size()[0] - 11),
                       random.randint(10, pixel_array.surface.get_size()[1] - 11))
            p1 = Point(random.randint(10, pixel_array.surface.get_size()[0] - 11),
                       random.randint(10, pixel_array.surface.get_size()[1] - 11))
            draw_line(p0, p1, pixel_array, COLOR_BLUE, True, COLOR_RANDOM(), COLOR_RANDOM())

    def random_circles():
        for _ in range(50):
            p0 = Point(random.randint(75, pixel_array.surface.get_size()[0] - 76), random.randint(75, pixel_array.surface.get_size()[1] - 76))
            draw_circle(p0, random.randint(3, 73), pixel_array, COLOR_RED)

    adjustable_triangle()
    # random_lines()
    # random_circles()
