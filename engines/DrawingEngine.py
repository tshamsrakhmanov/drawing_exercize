import pygame
from objects.InteractiveObjects import *
import math


class DrawingEngine:
    def __init__(self, drawing_coef: int):
        self.drawing_coef = drawing_coef

    def draw_window(self, pixel_array_input: pygame.PixelArray, objects_set: set):

        # iterate through list of objects
        for obj in objects_set:

            # based on the object - draw something
            if isinstance(obj, Dot):
                self.draw_point(Dot(obj.coordinate_x, obj.coordinate_y), pixel_array_input, obj.i_color)
            elif isinstance(obj, PinBoardCircle):
                match obj.active:
                    case True:
                        self.draw_circle_centerline(Dot(math.floor(obj.center_point.coordinate_x / self.drawing_coef),
                                                        math.floor(obj.center_point.coordinate_y / self.drawing_coef)),
                                                    obj.radius, pixel_array_input, obj.i_color)
                    case False:
                        self.draw_circle_centerline(Dot(math.floor(obj.center_point.coordinate_x / self.drawing_coef),
                                                        math.floor(obj.center_point.coordinate_y / self.drawing_coef)),
                                                    obj.radius, pixel_array_input, obj.i_color)
            elif isinstance(obj, Vector):
                obj: Vector

                vector_visible_length = 1000

                self.draw_line(obj.dot,
                               Dot(int(
                                   obj.dot.coordinate_x + vector_visible_length * math.cos(math.radians(obj.degree))),
                                   int(obj.dot.coordinate_y + vector_visible_length * math.sin(
                                       math.radians(obj.degree)))),
                               pixel_array_input, COLOR_RED,
                               False)
            elif isinstance(obj, MovableCircle):
                obj: MovableCircle
                # base implementation
                self.draw_circle_centerline(Dot(math.floor(obj.center_point.coordinate_x / self.drawing_coef),
                                                math.floor(obj.center_point.coordinate_y / self.drawing_coef)),
                                            obj.radius, pixel_array_input, obj.i_color)
            elif isinstance(obj, GradientCircle):
                self.draw_circle_centerline(Dot(math.floor(obj.center_point.coordinate_x / self.drawing_coef),
                                                math.floor(obj.center_point.coordinate_y / self.drawing_coef)),
                                            obj.actual_size, pixel_array_input, obj.i_color)
            elif isinstance(obj, ChainPiece):
                obj: ChainPiece

                self.draw_circle_centerline(Dot(math.floor(obj.center_point.coordinate_x / self.drawing_coef),
                                                math.floor(obj.center_point.coordinate_y / self.drawing_coef)),
                                            obj.link_size, pixel_array_input, obj.i_color)
            elif isinstance(obj, Circle):
                self.draw_circle_centerline(Dot(math.floor(obj.center_point.coordinate_x / self.drawing_coef),
                                                math.floor(obj.center_point.coordinate_y / self.drawing_coef)),
                                            obj.radius, pixel_array_input, obj.i_color)
            elif isinstance(obj, Line):
                self.draw_line(
                    obj.dot_start, obj.dot_end, pixel_array_input, obj.color, obj.is_pointed, obj.color_point_start,
                    obj.color_point_end)

    def draw_point(self, input_point: Dot, pixel_array: pygame.PixelArray,
                   input_color: RGBColor = COLOR_WHITE):
        """
        Add point drawing to the screen
        :param input_point: Point ( coordinates) to use as a center for drawing
        :param input_color: Color for point
        :param pixel_array: pixel_array
        :return: None
        """

        pixel_array[math.floor((input_point.coordinate_x + 1) / self.drawing_coef), math.floor(
            input_point.coordinate_y / self.drawing_coef)] = input_color
        pixel_array[math.floor((input_point.coordinate_x - 1) / self.drawing_coef), math.floor(
            input_point.coordinate_y / self.drawing_coef)] = input_color
        pixel_array[
            math.floor(input_point.coordinate_x / self.drawing_coef), math.floor(
                input_point.coordinate_y / self.drawing_coef)] = input_color
        pixel_array[math.floor(input_point.coordinate_x / self.drawing_coef), math.floor(
            (input_point.coordinate_y - 1) / self.drawing_coef)] = input_color
        pixel_array[math.floor(input_point.coordinate_x / self.drawing_coef), math.floor(
            (input_point.coordinate_y + 1) / self.drawing_coef)] = input_color

    # noinspection PyMethodMayBeStatic
    def draw_circle_centerline(self, point_center: Dot, radius: int, pixel_array: pygame.PixelArray,
                               color: RGBColor):
        x = radius
        y = 0
        err = 0
        while x >= y:
            # noinspection PyBroadException
            try:
                pixel_array[point_center.coordinate_x + x, point_center.coordinate_y + y] = color
                pixel_array[point_center.coordinate_x + y, point_center.coordinate_y + x] = color
                pixel_array[point_center.coordinate_x - y, point_center.coordinate_y + x] = color
                pixel_array[point_center.coordinate_x - x, point_center.coordinate_y + y] = color
                pixel_array[point_center.coordinate_x - x, point_center.coordinate_y - y] = color
                pixel_array[point_center.coordinate_x - y, point_center.coordinate_y - x] = color
                pixel_array[point_center.coordinate_x + y, point_center.coordinate_y - x] = color
                pixel_array[point_center.coordinate_x + x, point_center.coordinate_y - y] = color
            except Exception:
                pass

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

        x0 = point_start.coordinate_x
        x1 = point_end.coordinate_x
        y0 = point_start.coordinate_y
        y1 = point_end.coordinate_y

        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -1 * abs(y1 - y0)
        sy = 1 if y0 < y1 else -1

        error = dx + dy

        while True:
            # noinspection PyBroadException
            try:
                pixel_array[
                    math.floor((x0 - 1) / self.drawing_coef), math.floor((y0 - 1) / self.drawing_coef)] = color_of_line
            except Exception:
                pass

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
