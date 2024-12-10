from settings import resolution
import pygame
from objects.InteractiveObjects import *


class DrawingEngine:
    def __init__(self):
        pass

    def draw_window(self, pixel_array_input: pygame.PixelArray, objects_set: set):
        # iterate through list of objects
        for obj in objects_set:

            # based on the object - draw something

            if isinstance(obj, Dot):
                self.draw_point(Dot(obj.x, obj.y), pixel_array_input, obj.color)
            elif isinstance(obj, InteractiveCircle):
                match obj.active:
                    case True:
                        self.draw_circle_centerline(Dot(obj.dot_start.x, obj.dot_start.y),
                                                    obj.radius + 15, pixel_array_input, obj.color)
                    case False:
                        self.draw_circle_centerline(Dot(obj.dot_start.x, obj.dot_start.y),
                                                    obj.radius, pixel_array_input, obj.color)
            elif isinstance(obj, Circle):
                self.draw_circle_centerline(
                    Dot(obj.dot_start.x, obj.dot_start.y), obj.radius, pixel_array_input, obj.color)
            elif isinstance(obj, Line):
                self.draw_line(
                    obj.dot_start, obj.dot_end, pixel_array_input, obj.color, obj.is_pointed, obj.color_point_start,
                    obj.color_point_end)

    # @staticmethod
    def draw_circle(self, point: Dot, radius: int, pixel_array: pygame.pixelarray, input_color: RGBColor = COLOR_WHITE):
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

                    if self.is_in_array(dx + point.x, dy + point.y):
                        pixel_array[dx + point.x, dy + point.y] = input_color
                    if self.is_in_array(dx + point.x, -dy + point.y):
                        pixel_array[dx + point.x, -dy + point.y] = input_color
                    if self.is_in_array(-dx + point.x, dy + point.y):
                        pixel_array[-dx + point.x, dy + point.y] = input_color
                    if self.is_in_array(-dx + point.x, -dy + point.y):
                        pixel_array[-dx + point.x, -dy + point.y] = input_color

    @staticmethod
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

    @staticmethod
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

    # @staticmethod
    def draw_line(self, point_start: Dot, point_end: Dot, pixel_array: pygame.PixelArray,
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
            self.draw_point(point_start, pixel_array, color_start)
            self.draw_point(point_end, pixel_array, color_end)

    @staticmethod
    def is_in_array(x_input, y_input):
        if 0 < x_input - 1 < resolution.width - 1 and 0 < y_input - 1 < resolution.height - 1:
            return True
        return False
