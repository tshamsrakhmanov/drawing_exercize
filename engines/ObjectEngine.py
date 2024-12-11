import math
import random

# import settings.resolution
from objects.InteractiveObjects import PinBoardCircle, GradientCircle, MovableCircle, Vector
from objects.GeometryObjects import Geometry, Dot
from settings.colors import *


class ObjectsEngine:
    # to resolve out-of bounds movement
    BOUNDARY = 500

    def __init__(self, WIDTH: int, HEIGHT: int, coef: int):
        """
        Init of objects engine
         - create empty set of objects
         - t.b.d. later with additional info
        """
        self.set_of_objects = set()
        self.ticker_cache = None
        self.limit_x = WIDTH * coef
        self.limit_y = HEIGHT * coef

    def get_field(self):
        return self.limit_x, self.limit_y

    def update_set_of_objects(self, mouse_pos: tuple, mouse_up: bool, mouse_down: bool, dt: int):
        """
        By evoking this method ObjectEngine will update status and all relevant parameters of all objects in modeling space
        :param mouse_pos: provide coordinates of mouse position on the screen
        :param mouse_up: detection of mouse release button
        :param mouse_down: detection of mouse press button
        :return: None
        """

        for obj in self.set_of_objects:

            if isinstance(obj, GradientCircle):

                """
                GRADIENT CIRCLE FACILITATION
                Sort-of-implementation due to enormous volume of fine tuning
                This values of proportions are tested /good/ with following matrix:

                '
                distance = 40

                for i in range(1, 38): # 38
                    for y in range(1, 19): # 19
                        temp_dot = Dot(distance * i, distance * y)
                        objects_buffer.append(
                            GradientCircle(i_dot=temp_dot, i_radius=10, i_color=COLOR_WHITE))
                '
                """

                distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

                max_dist = 40
                min_dist = 1
                delta_dist = max_dist - min_dist

                if distance >= obj.radius * max_dist:
                    obj.actual_size = obj.radius * 2
                    obj.color = COLOR_GREEN
                elif obj.radius * min_dist <= distance < obj.radius * max_dist:
                    coeff_1 = (distance - min_dist * obj.radius) / (delta_dist * obj.radius)
                    obj.actual_size = int(
                        (obj.radius / 2) + (1.5 * obj.radius) * coeff_1)
                    obj.color = (int(255 - 255 * coeff_1), int(0 + 255 * coeff_1), 0)
                else:
                    obj.actual_size = int(obj.radius / 4)
                    obj.color = COLOR_RED
            elif isinstance(obj, PinBoardCircle):
                distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

                # Feature - focus light of active / inactive circle - p.1
                if distance < obj.radius:
                    if obj.active is False:
                        if obj.focus_non_active_ready:
                            obj.focus_non_active_ready = False
                            obj.color = obj.color_non_active_focused
                    if obj.active is True:
                        if obj.focus_active_ready:
                            obj.focus_active_ready = False
                            obj.color = obj.color_active_focused

                # Feature - focus light of active / inactive circle - p.2
                if distance > obj.radius:
                    if obj.active is False:
                        obj.color = obj.color_non_active_non_focused
                        obj.focus_non_active_ready = True
                    if obj.active is True:
                        obj.color = obj.color_active_non_focused
                        obj.focus_active_ready = True

                # snapping Interactive Circle to mouse cursor while active = True
                if obj.movable and obj.active:
                    obj.color = obj.color_active_focused
                    obj.dot_start.x = mouse_pos[0]
                    obj.dot_start.y = mouse_pos[1]

                # change status of Interactive circle by mouse click
                if mouse_up:
                    if distance < obj.radius:
                        if obj.active:
                            obj.active = False
                        else:
                            obj.active = True
            elif isinstance(obj, MovableCircle):
                obj: MovableCircle

                # apply sectoring
                if obj.dot_start.x < int(self.limit_x / 2):
                    obj.sector = 1
                else:
                    obj.sector = 2

                energy_loss = 0.85
                # energy_loss = 1

                if obj.dot_start.y < ObjectsEngine.BOUNDARY:
                    obj.vector.energy *= energy_loss
                    obj.dot_start.y = ObjectsEngine.BOUNDARY
                    obj.vector.degree = self.mirror_angle_by_x_axis(obj.vector.degree)
                elif obj.dot_start.y > self.limit_y - ObjectsEngine.BOUNDARY:
                    obj.vector.energy *= energy_loss
                    obj.dot_start.y = self.limit_y - ObjectsEngine.BOUNDARY
                    obj.vector.degree = self.mirror_angle_by_x_axis(obj.vector.degree)
                elif obj.dot_start.x < ObjectsEngine.BOUNDARY:
                    obj.vector.energy *= energy_loss
                    obj.dot_start.x = ObjectsEngine.BOUNDARY + 1
                    obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)
                elif obj.dot_start.x > self.limit_x - ObjectsEngine.BOUNDARY:
                    obj.vector.energy *= energy_loss
                    obj.dot_start.x = self.limit_x - ObjectsEngine.BOUNDARY - 1
                    obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)

                # obj.vector.energy -= 0.075
                obj.vector.energy -= 1

                obj.vector.energy = round(obj.vector.energy, 3)

                if obj.vector.energy > 0:
                    obj.vector.dot.x += math.floor(
                        (dt *  (obj.vector.energy / 100)) * math.cos(math.radians(obj.vector.degree)))
                    obj.vector.dot.y += math.floor(
                        (dt * (obj.vector.energy / 100)) * math.sin(math.radians(obj.vector.degree)))


    def get_set_of_objects(self):
        """
        Set of objects will be returned
        :return:Set of objects
        """
        return self.set_of_objects

    def add_object(self, input_object: Geometry):
        self.set_of_objects.add(input_object)

    def remove_object(self, input_object: Geometry):
        self.set_of_objects.remove(input_object)

    @staticmethod
    def mirror_angle_by_y_axis(a):

        if a < 0:
            return a * -1

        if a > 360:
            return a - 360

        if a == 0:
            answer = 180
        elif a == 90:
            answer = 270
        elif a == 180:
            answer = 0
        elif a == 270:
            answer = 180
        elif a == 360:
            answer = 180

        # I - II
        if 0 < a < 90:
            answer = 180 - a
        # II - I
        elif 90 < a < 180:
            answer = a - 2 * (a - 90)

        # III - IV
        if 180 < a < 270:
            answer = 540 - a
        elif 270 < a < 360:
            answer = 540 - a
        # return answer + random.randint(0, 15)
        return answer + 1

    @staticmethod
    def mirror_angle_by_x_axis(a):

        if a < 0:
            return a * -1

        if a > 360:
            return a - 360

        if a == 0:
            answer = 180
        elif a == 90:
            answer = 270
        elif a == 180:
            answer = 0
        elif a == 270:
            answer = 180
        elif a == 360:
            answer = 180

        # I - IV
        if 0 < a < 90:
            answer = 360 - a
        # IV - I
        elif 270 < a < 360:
            answer = 360 - a

        # II - III
        if 90 < a < 180:
            answer = 360 - a
        # III - II
        elif 180 < a < 270:
            answer = 360 - a

        # return answer + random.randint(0, 15)
        return answer + 1
