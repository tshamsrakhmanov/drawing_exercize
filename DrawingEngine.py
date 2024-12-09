import settings
from GeometryClasses import *
from settings import *
import pygame
from InteractiveObjects import *


def draw_window(pixel_array: pygame.pixelarray, objects_notation: dict):
    def adjustable_triangle():

        radius = 15

        p1 = Dot(50, 50)
        p2 = Dot(250, 250)
        p3 = Dot(350, 100)

        draw_circle(p1, radius, pixel_array, COLOR_RED)
        draw_circle(p2, radius, pixel_array, COLOR_RED)
        draw_circle(p3, radius, pixel_array, COLOR_RED)
        draw_line(p1, p2, pixel_array, COLOR_RED)
        draw_line(p2, p3, pixel_array, COLOR_RED)
        draw_line(p1, p3, pixel_array, COLOR_RED)

        if pygame.mouse.get_focused():
            p0 = Dot(*pygame.mouse.get_pos())
            draw_circle(p0, radius, pixel_array, COLOR_WHITE)
            draw_line(p0, p1, pixel_array, COLOR_WHITE)
            draw_line(p0, p2, pixel_array, COLOR_WHITE)
            draw_line(p0, p3, pixel_array, COLOR_WHITE)

    def random_lines(count):
        for _ in range(count):
            draw_line(Dot(random.randint(10, pixel_array.surface.get_size()[0] - 11),
                          random.randint(10, pixel_array.surface.get_size()[1] - 11)),
                      Dot(random.randint(10, pixel_array.surface.get_size()[0] - 11),
                          random.randint(10, pixel_array.surface.get_size()[1] - 11)), pixel_array, COLOR_BLUE, True,
                      COLOR_RANDOM(), COLOR_RANDOM())

    def random_circles(count):
        for _ in range(count):
            p0 = Dot(random.randint(75, pixel_array.surface.get_size()[0] - 76),
                     random.randint(75, pixel_array.surface.get_size()[1] - 76))
            draw_circle(p0, random.randint(3, 73), pixel_array, COLOR_RANDOM())

    def test_of_centerline_circle():
        p0 = Dot(200, 200)
        draw_circle_centerline(p0, 40, pixel_array, COLOR_RED)

    def random_full_circles(count):

        min_radius = 5
        max_radius = 75
        gap = 1

        for _ in range(count):
            p0 = Dot(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                     random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))
            draw_circle_centerline(p0, random.randint(min_radius, max_radius), pixel_array, COLOR_RANDOM())

    def triplets(count):
        def triplets_generation():
            min_radius = 5
            max_radius = 75
            gap = 1

            p0 = Dot(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                     random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))
            p1 = Dot(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                     random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))
            p2 = Dot(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                     random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))

            draw_circle_centerline(p0, random.randint(min_radius, max_radius), pixel_array, COLOR_WHITE)
            draw_circle_centerline(p1, random.randint(min_radius, max_radius), pixel_array, COLOR_WHITE)
            draw_circle_centerline(p2, random.randint(min_radius, max_radius), pixel_array, COLOR_WHITE)
            draw_line(p0, p1, pixel_array, COLOR_GREEN)
            draw_line(p1, p2, pixel_array, COLOR_GREEN)
            draw_line(p2, p0, pixel_array, COLOR_GREEN)

        for _ in range(count):
            triplets_generation()

    # adjustable_triangle()
    # random_lines(100)
    # random_circles(100)
    # test_of_centerline_circle()
    # random_full_circles(300)
    # triplets(15)

    for obj in objects_notation:

        if isinstance(obj, Dot):
            draw_point(Dot(obj.x, obj.y), pixel_array, obj.color)
        elif isinstance(obj, InteractiveCircle):
            match obj.state:
                case True:
                    draw_circle_centerline(Dot(obj.dot_start.x, obj.dot_start.y),
                                           obj.radius, pixel_array, obj.color)
                case False:
                    draw_circle_centerline(Dot(obj.dot_start.x, obj.dot_start.y),
                                           obj.radius + 15, pixel_array, COLOR_RED)
        elif isinstance(obj, Circle):
            draw_circle_centerline(Dot(obj.dot_start.x, obj.dot_start.y), obj.radius, pixel_array, obj.color)



def draw_circle(point: Dot, radius: int, pixel_array: pygame.pixelarray, input_color: RGBColor = COLOR_WHITE):
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


def draw_point(input_point: Dot, pixel_array: pygame.PixelArray,
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


def draw_circle_centerline(point_center: Dot, radius: int, pixel_array: pygame.PixelArray,
                           color: RGBColor):
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


def draw_line(point_start: Dot, point_end: Dot, pixel_array: pygame.PixelArray,
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
