import math

from objects.InteractiveObjects import *


class ObjectsEngine:
    def __init__(self):
        self.set_of_objects = set()
        self.readiness = True
        self.counter_mouse = 0
        self.click = False

    def update_set_of_objects(self, mouse_pos: tuple, mouse_up: bool, mouse_down: bool, counter: int):

        # changing ACTIVE | NON-ACTIVE for Interactive circles with mouse click
        if mouse_up:

            for obj in filter(lambda x: isinstance(x, InteractiveCircle), self.set_of_objects):
                distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

                if distance < 30:
                    if obj.active:
                        obj.active = False
                    else:
                        obj.active = True

        # changing focus on active | non-active Interactive circles
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
        return self.set_of_objects

    def add_object(self, input_object: Geometry):
        self.set_of_objects.add(input_object)

    def remove_object(self, input_object: Geometry):
        self.set_of_objects.remove(input_object)
