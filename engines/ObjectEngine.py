import math

from objects.InteractiveObjects import *


class ObjectsEngine:
    def __init__(self):
        self.set_of_objects = set()
        self.readiness = True

    def update_set_of_objects(self, mouse_pos: tuple):
        # SOME MAGIC TO UPDATE OBJECT STATEMENTS

        for obj in filter(lambda x: isinstance(x, InteractiveCircle), self.set_of_objects):
            distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

            if distance < 30:
                obj.state = False
            else:
                obj.state = True

    def get_set_of_objects(self):
        return self.set_of_objects

    def add_object(self, input_object: Geometry):
        self.set_of_objects.add(input_object)

    def remove_object(self, input_object: Geometry):
        self.set_of_objects.remove(input_object)


