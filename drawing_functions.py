import pygame
from additional_types import *
from colors import *
import settings


def draw_circle(point: Point, radius: int, pixel_array: pygame.pixelarray, input_color: RGBColor = COLOR_WHITE):
    """
    Add circle (filled) to the screen
    :param point: Center point of circle
    :param radius: Radius of circle in pixels
    :param pixel_array: pixel_array to draw a circle
    :param input_color: Color for drawing
    :return: None
    """
    for dx in range(radius):
        for dy in range(radius):
            if dx ** 2 + dy ** 2 <= radius ** 2:

                if is_in_array(dx + point.x, dy + point.y):
                    pixel_array[dx + point.x, dy + point.y] = input_color
                if is_in_array(dx + point.x, -dy + point.y):
                    pixel_array[dx + point.x, -dy + point.y] = input_color
                if is_in_array(-dx + point.x, dy + point.y):
                    pixel_array[-dx + point.x, dy + point.y] = input_color
                if is_in_array(-dx + point.x, -dy + point.y):
                    pixel_array[-dx + point.x, -dy + point.y] = input_color


def draw_point(input_point: Point, pixel_array: pygame.PixelArray,
               input_color: RGBColor = COLOR_WHITE):
    """
    Add point drawing to the screen
    :param input_point: Point ( coordinates) to use as a center for drawing
    :param input_color: Color for point
    :param pixel_array: pixel_array
    :return: None
    """

    pixel_array[input_point.x + 1, input_point.y] = input_color
    pixel_array[input_point.x - 1, input_point.y] = input_color
    pixel_array[input_point.x, input_point.y] = input_color
    pixel_array[input_point.x, input_point.y - 1] = input_color
    pixel_array[input_point.x, input_point.y + 1] = input_color


def draw_circle_centerline(point_center: Point, radius: int, pixel_array: pygame.PixelArray,
                           color: RGBColor = COLOR_WHITE):
    # draw center point of the circle
    pixel_array[point_center.x, point_center.y] = color

    x = radius
    y = 0
    err = 0
    while x >= y:
        pixel_array[point_center.x + x, point_center.y + y] = color
        pixel_array[point_center.x + y, point_center.y + x] = color
        pixel_array[point_center.x - y, point_center.y + x] = color
        pixel_array[point_center.x - x, point_center.y + y] = color
        pixel_array[point_center.x - x, point_center.y - y] = color
        pixel_array[point_center.x - y, point_center.y - x] = color
        pixel_array[point_center.x + y, point_center.y - x] = color
        pixel_array[point_center.x + x, point_center.y - y] = color

        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x


def draw_line(point_start: Point, point_end: Point, pixel_array: pygame.PixelArray,
              color_of_line: RGBColor = COLOR_WHITE,
              pointed=False, color_start: RGBColor = COLOR_WHITE, color_end: RGBColor = COLOR_WHITE):
    """
    Implementation of algorythm declared in article:
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    :param point_start: Start point
    :param point_end: End point
    :param color_of_line: Color, by which line will be drawn
    :param pixel_array: pixel_array
    :param pointed: If true - end and start of line will be drawn with points
    :param color_start: If pointed true - declare desired color of end point
    :param color_end: If pointed true - declare desired color of start point
    :return: None
    """

    x0 = point_start.x
    x1 = point_end.x
    y0 = point_start.y
    y1 = point_end.y

    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -1 * abs(y1 - y0)
    sy = 1 if y0 < y1 else -1

    error = dx + dy

    while True:

        pixel_array[x0 - 1, y0 - 1] = color_of_line

        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * error
        if e2 >= dy:
            error += dy
            x0 += sx
        if e2 <= dx:
            error += dx
            y0 += sy

    if pointed:
        draw_point(point_start, pixel_array, color_start)
        draw_point(point_end, pixel_array, color_end)


def tdc(x_input: int, y_input: int):
    """
    Convert Decard-oriented coordinates to screen-oriented coordinates
    (center of a screen as 0;0 and x from left to right, y from bottom to top)
    :param x_input: Coordinate of X in Decard coordinate system
    :param y_input: Coordinate of Y in Decard coordinate system
    :return: tuple (A,B) where A - x-coord in screen coordinate system, b - y-coord in screen coordinate system
    """

    return int(settings.width / 2) + x_input, int(settings.height / 2) - y_input


def is_in_array(x_input, y_input):
    if 0 < x_input - 1 < settings.width - 1 and 0 < y_input - 1 < settings.height - 1:
        return True
    return False
