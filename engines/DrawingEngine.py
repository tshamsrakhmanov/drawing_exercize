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
                                                    obj.radius, pixel_array_input, COLOR_GREEN)
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
            elif isinstance(obj, BezierContainer):

                interpolation_steps = 30

                if len(obj) == 3:

                    bezier_interpolation_points_list = []

                    # naming of points for easier understanding
                    base_point = list(obj)[0]
                    anchor = list(obj)[1]
                    finish_point = list(obj)[2]

                    # calculate angle base-to-anchor (to calculate portions)
                    raw_angle_base_to_anchor = round(self.negative_to_positive(math.degrees(
                        math.atan2(anchor.coordinate_y - base_point.coordinate_y,
                                   anchor.coordinate_x - base_point.coordinate_x))), 3)

                    # calculate angle anchor-to-finish (to calculate portions)
                    raw_angle_anchor_to_finish = round(self.negative_to_positive(math.degrees(
                        math.atan2(finish_point.coordinate_y - anchor.coordinate_y,
                                   finish_point.coordinate_x - anchor.coordinate_x))), 3)

                    # calculate len from base to anchor
                    len_base_to_anchor = math.sqrt((base_point.coordinate_x - anchor.coordinate_x) ** 2 +
                                                   (base_point.coordinate_y - anchor.coordinate_y) ** 2)
                    # calculate len from anchor to finish
                    len_anchor_to_finish = math.sqrt((anchor.coordinate_x - finish_point.coordinate_x) ** 2 +
                                                     (anchor.coordinate_y - finish_point.coordinate_y) ** 2)

                    # add first point
                    bezier_interpolation_points_list.append(
                        Dot(round(list(obj)[0].coordinate_x), round(list(obj)[0].coordinate_y),
                            COLOR_GREEN))

                    # add intermediate (interpolated) points
                    for i in range(1, interpolation_steps + 1):
                        # make point by 0.1 ... 0.9 of length from base to anchor
                        temp_point_1 = Dot(round(
                            base_point.coordinate_x + len_base_to_anchor * (i / interpolation_steps) * math.cos(
                                math.radians(raw_angle_base_to_anchor))),
                            round(base_point.coordinate_y + len_base_to_anchor * (
                                    i / interpolation_steps) * math.sin(
                                math.radians(raw_angle_base_to_anchor))))

                        # make point by 0.1 ... 0.9 of length from anchor to finish
                        temp_point_2 = Dot(round(
                            anchor.coordinate_x + len_anchor_to_finish * (i / interpolation_steps) * math.cos(
                                math.radians(raw_angle_anchor_to_finish))),
                            round(anchor.coordinate_y + len_anchor_to_finish * (
                                    i / interpolation_steps) * math.sin(
                                math.radians(raw_angle_anchor_to_finish))))

                        # calculate angle, given line made of 2 temp points (to know, in which direction shift)
                        raw_angle_internal = round(self.negative_to_positive(math.degrees(
                            math.atan2(temp_point_2.coordinate_y - temp_point_1.coordinate_y,
                                       temp_point_2.coordinate_x - temp_point_1.coordinate_x))), 3)

                        # length b/w two temp points
                        len_internal = math.sqrt((temp_point_1.coordinate_x - temp_point_2.coordinate_x) ** 2 +
                                                 (temp_point_1.coordinate_y - temp_point_2.coordinate_y) ** 2)

                        # make point in 0.1 ... 0.9 on line b/w two temp points
                        new_temp_point = Dot(round(
                            temp_point_1.coordinate_x + len_internal * (i / interpolation_steps) * math.cos(
                                math.radians(raw_angle_internal))),
                            round(temp_point_1.coordinate_y + len_internal * (
                                    i / interpolation_steps) * math.sin(
                                math.radians(raw_angle_internal))), COLOR_GREEN)

                        bezier_interpolation_points_list.append(new_temp_point)

                    # add last point
                    bezier_interpolation_points_list.append(
                        Dot(round(list(obj)[2].coordinate_x), round(list(obj)[2].coordinate_y),
                            COLOR_GREEN))

                    # drawing points instead of lines
                    # -------------------------------
                    # for pos in bezier_interpolation_points_list:
                    #     self.draw_point(Dot(pos.coordinate_x, pos.coordinate_y), pixel_array_input, pos.i_color)

                    # drawing interpolated lines
                    # --------------------------
                    for i in range(1, len(bezier_interpolation_points_list)):
                        act_point = bezier_interpolation_points_list[i]
                        next_point = bezier_interpolation_points_list[i - 1]
                        self.draw_line(act_point, next_point, pixel_array_input, COLOR_WHITE)

                    self.draw_line(base_point, anchor, pixel_array_input, COLOR_GREY)
                    self.draw_line(finish_point, anchor, pixel_array_input, COLOR_GREY)

                elif len(obj) == 4:

                    bezier_points_list = list(obj)

                    # naming of points inside of container just to make it easier
                    head = bezier_points_list[0]
                    adj1 = bezier_points_list[1]
                    adj2 = bezier_points_list[2]
                    tail = bezier_points_list[3]

                    # draw first interpolated points
                    ang_head_adj1 = round(self.negative_to_positive(math.degrees(
                        math.atan2(adj1.coordinate_y - head.coordinate_y,
                                   adj1.coordinate_x - head.coordinate_x))), 3)

                    ang_adj2_adj1 = round(self.negative_to_positive(math.degrees(
                        math.atan2(adj2.coordinate_y - adj1.coordinate_y,
                                   adj2.coordinate_x - adj1.coordinate_x))), 3)

                    ang_tail_adj2 = round(self.negative_to_positive(math.degrees(
                        math.atan2(tail.coordinate_y - adj2.coordinate_y,
                                   tail.coordinate_x - adj2.coordinate_x))), 3)

                    len_head_to_adj1 = math.sqrt((head.coordinate_x - adj1.coordinate_x) ** 2 +
                                                 (head.coordinate_y - adj1.coordinate_y) ** 2)
                    len_adj1_to_adj2 = math.sqrt((adj2.coordinate_x - adj1.coordinate_x) ** 2 +
                                                 (adj2.coordinate_y - adj1.coordinate_y) ** 2)
                    len_adj2_to_tail = math.sqrt((tail.coordinate_x - adj2.coordinate_x) ** 2 +
                                                 (tail.coordinate_y - adj2.coordinate_y) ** 2)

                    interpolated_lv3_points_list = [head]

                    for i in range(1, interpolation_steps + 1):
                        # make point by 0.1 ... 0.9 of length from base to anchor
                        temp_point_1 = Dot(round(
                            head.coordinate_x + len_head_to_adj1 * (i / interpolation_steps) * math.cos(
                                math.radians(ang_head_adj1))),
                                           round(head.coordinate_y + len_head_to_adj1 * (
                                                       i / interpolation_steps) * math.sin(
                                               math.radians(ang_head_adj1))))

                        temp_point_2 = Dot(round(
                            adj1.coordinate_x + len_adj1_to_adj2 * (i / interpolation_steps) * math.cos(
                                math.radians(ang_adj2_adj1))),
                                           round(adj1.coordinate_y + len_adj1_to_adj2 * (
                                                       i / interpolation_steps) * math.sin(
                                               math.radians(ang_adj2_adj1))))

                        temp_point_3 = Dot(round(
                            adj2.coordinate_x + len_adj2_to_tail * (i / interpolation_steps) * math.cos(
                                math.radians(ang_tail_adj2))),
                                           round(adj2.coordinate_y + len_adj2_to_tail * (
                                                       i / interpolation_steps) * math.sin(
                                               math.radians(ang_tail_adj2))))

                        ang_t2_t1 = round(self.negative_to_positive(
                            math.degrees(math.atan2(temp_point_2.coordinate_y - temp_point_1.coordinate_y,
                                                    temp_point_2.coordinate_x - temp_point_1.coordinate_x))), 3)

                        ang_t3_t2 = round(self.negative_to_positive(
                            math.degrees(math.atan2(temp_point_3.coordinate_y - temp_point_2.coordinate_y,
                                                    temp_point_3.coordinate_x - temp_point_2.coordinate_x))), 3)

                        len_t2_to_t1 = math.sqrt((temp_point_2.coordinate_x - temp_point_1.coordinate_x) ** 2 +
                                                 (temp_point_2.coordinate_y - temp_point_1.coordinate_y) ** 2)

                        len_t3_to_t2 = math.sqrt((temp_point_3.coordinate_x - temp_point_2.coordinate_x) ** 2 +
                                                 (temp_point_3.coordinate_y - temp_point_2.coordinate_y) ** 2)

                        temp_point_4 = Dot(round(
                            temp_point_1.coordinate_x + len_t2_to_t1 * (i / interpolation_steps) * math.cos(
                                math.radians(ang_t2_t1))),
                                           round(temp_point_1.coordinate_y + len_t2_to_t1 * (
                                                       i / interpolation_steps) * math.sin(math.radians(ang_t2_t1))))

                        temp_point_5 = Dot(round(
                            temp_point_2.coordinate_x + len_t3_to_t2 * (i / interpolation_steps) * math.cos(
                                math.radians(ang_t3_t2))),
                                           round(temp_point_2.coordinate_y + len_t3_to_t2 * (
                                                       i / interpolation_steps) * math.sin(math.radians(ang_t3_t2))))

                        ang_t5_t4 = round(self.negative_to_positive(
                            math.degrees(math.atan2(temp_point_5.coordinate_y - temp_point_4.coordinate_y,
                                                    temp_point_5.coordinate_x - temp_point_4.coordinate_x))), 3)

                        len_t5_to_t4 = math.sqrt((temp_point_5.coordinate_x - temp_point_4.coordinate_x) ** 2 +
                                                 (temp_point_5.coordinate_y - temp_point_4.coordinate_y) ** 2)

                        temp_point_6 = Dot(round(
                            temp_point_4.coordinate_x + len_t5_to_t4 * (i / interpolation_steps) * math.cos(
                                math.radians(ang_t5_t4))),
                                           round(temp_point_4.coordinate_y + len_t5_to_t4 * (
                                                       i / interpolation_steps) * math.sin(math.radians(ang_t5_t4))))

                        interpolated_lv3_points_list.append(temp_point_6)

                    interpolated_lv3_points_list.append(tail)

                    # drawing adjustment anchor lines
                    # --------------------------
                    self.draw_line(head, adj1, pixel_array_input, COLOR_GREY)
                    self.draw_line(tail, adj2, pixel_array_input, COLOR_GREY)

                    # drawing interpolated lines
                    # --------------------------
                    for i in range(1, len(interpolated_lv3_points_list)):
                        act_point = interpolated_lv3_points_list[i]
                        next_point = interpolated_lv3_points_list[i - 1]
                        self.draw_line(act_point, next_point, pixel_array_input, COLOR_WHITE)

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
        pixel_array[math.floor(input_point.coordinate_x / self.drawing_coef), math.floor(
            input_point.coordinate_y / self.drawing_coef)] = input_color
        pixel_array[math.floor(input_point.coordinate_x / self.drawing_coef), math.floor(
            (input_point.coordinate_y - 1) / self.drawing_coef)] = input_color
        pixel_array[math.floor(input_point.coordinate_x / self.drawing_coef), math.floor(
            (input_point.coordinate_y + 1) / self.drawing_coef)] = input_color

        pixel_array[math.floor((input_point.coordinate_x - 1) / self.drawing_coef), (
                    math.floor(input_point.coordinate_y - 1) / self.drawing_coef)] = input_color
        pixel_array[math.floor((input_point.coordinate_x + 1) / self.drawing_coef), (
                    math.floor(input_point.coordinate_y + 1) / self.drawing_coef)] = input_color
        pixel_array[math.floor((input_point.coordinate_x - 1) / self.drawing_coef), (
                    math.floor(input_point.coordinate_y + 1) / self.drawing_coef)] = input_color
        pixel_array[math.floor((input_point.coordinate_x + 1) / self.drawing_coef), (
                    math.floor(input_point.coordinate_y - 1) / self.drawing_coef)] = input_color

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

        x0 = round(point_start.coordinate_x)
        x1 = round(point_end.coordinate_x)
        y0 = round(point_start.coordinate_y)
        y1 = round(point_end.coordinate_y)

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

    @staticmethod
    def negative_to_positive(a):
        angle = a % 360
        if angle < 0:
            angle += 360
        return angle
