import math

from objects.InteractiveObjects import MovableCircle, GradientCircle
from objects.GeometryObjects import Geometry
from settings.colors import *


class ObjectsEngine:

    def __init__(self):
        """
        Init of objects engine
         - create empty set of objects
         - t.b.d. later with additional info
        """
        self.set_of_objects = set()

    @staticmethod
    def coloring_gradient_circle(input_proportion: float):
        print(input_proportion)
        if 0 < input_proportion < 1:
            r = input_proportion * 255
            g = input_proportion * 255
            b = 0
        else:
            r = 255
            g = 255
            b = 255
        return r, g, b

    def update_set_of_objects(self, mouse_pos: tuple, mouse_up: bool, mouse_down: bool):
        """
        By evoking this method ObjectEngine will update status and all relevant parameters of all objects in modeling space
        :param mouse_pos: provide coordinates of mouse position on the screen
        :param mouse_up: detection of mouse release button
        :param mouse_down: detection of mouse press button
        :return: None
        """

        # GRADIENT CIRCLE FACILITATION
        """
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
        for obj in filter(lambda x: isinstance(x, GradientCircle), self.set_of_objects):
            obj: GradientCircle
            distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

            if distance >= obj.radius * 50:
                obj.actual_size = obj.radius * 2
            elif obj.radius * 4 <= distance < obj.radius * 50:
                obj.actual_size = int(
                    (obj.radius / 2) + (1.5 * obj.radius) * (distance - 8 * obj.radius) / (46 * obj.radius))
            else:
                obj.actual_size = int(obj.radius / 4)

        # MOVABLE CIRCLE FACILITATION
        for obj in filter(lambda x: isinstance(x, MovableCircle), self.set_of_objects):

            obj: MovableCircle
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
                obj.dot_start.x = mouse_pos[0]
                obj.dot_start.y = mouse_pos[1]

            # change status of Interactive circle by mouse click
            if mouse_up:
                if distance < obj.radius:
                    if obj.active:
                        obj.active = False
                    else:
                        obj.active = True

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
