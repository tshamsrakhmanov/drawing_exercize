from GeometryClasses import *


class ObjectsEngine:
    def __init__(self):
        self.objects_notation = set()
        self.readiness = True

    def update_objects_state(self, mouse_up: bool, mouse_pos: tuple):
        # SOME MAGIC TO UPDATE OBJECT STATEMENTS

        return self.objects_notation

    def add_object(self, input_object: Geometry):
        self.objects_notation.add(input_object)

    def remove(self, input_object: Geometry):
        self.objects_notation.remove(input_object)
