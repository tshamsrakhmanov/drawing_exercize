import math

from GeometryClasses import *
from InteractiveObjects import *


class ObjectsEngine:
    def __init__(self):
        self.objects_notation = set()
        self.readiness = True

    def objects_state(self, mouse_pos: tuple):
        # SOME MAGIC TO UPDATE OBJECT STATEMENTS

        for obj in filter(lambda x: isinstance(x, InteractiveCircle), self.objects_notation):
            distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

            if distance < 30:
                obj.state = False
            else:
                obj.state = True

        return self.objects_notation

    def add_object(self, input_object: Geometry):
        self.objects_notation.add(input_object)

    def remove_object(self, input_object: Geometry):
        self.objects_notation.remove(input_object)


