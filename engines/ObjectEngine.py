import math

from objects.InteractiveObjects import InteractiveCircle
from objects.GeometryObjects import Geometry


class ObjectsEngine:

    def __init__(self):
        """
        Init of objects engine
         - create empty set of objects
         - t.b.d. later with additional info
        """
        self.set_of_objects = set()

    def update_set_of_objects(self, mouse_pos: tuple, mouse_up: bool, mouse_down: bool):
        """
        By evoking this method ObjectEngine will update status and all relevant parameters of all objects in modeling space
        :param mouse_pos: provide coordinates of mouse position on the screen
        :param mouse_up: detection of mouse release button
        :param mouse_down: detection of mouse press button
        :return: None
        """
        # INTERRUPT BY MOUSE CLICK
        if mouse_up:

            # changing ACTIVE | NON-ACTIVE for Interactive circles with mouse click
            for obj in filter(lambda x: isinstance(x, InteractiveCircle), self.set_of_objects):
                distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

                if distance < 30:
                    if obj.active:
                        obj.active = False
                    else:
                        obj.active = True

                # self.remove_object(obj)

        # HOVERING OF INTERACTIVE CIRCLES
        for obj in filter(lambda x: isinstance(x, InteractiveCircle), self.set_of_objects):
            distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

            if distance < obj.radius:
                if obj.active is False:
                    if obj.focus_non_active_ready:
                        obj.focus_non_active_ready = False
                        obj.color = obj.color_non_active_focused
                if obj.active is True:
                    if obj.focus_active_ready:
                        obj.focus_active_ready = False
                        obj.color = obj.color_active_focused

            if distance > obj.radius:
                if obj.active is False:
                    obj.color = obj.color_non_active_non_focused
                    obj.focus_non_active_ready = True
                if obj.active is True:
                    obj.color = obj.color_active_non_focused
                    obj.focus_active_ready = True

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
