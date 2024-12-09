import random
from dataclasses import dataclass
import math


@dataclass
class Point:
    """
    Class to determine object-related coordinates
    """
    x: int
    y: int


@dataclass
class RGBColor:
    r: int
    g: int
    b: int


class SomeObject:
    def __init__(self, name_input):
        self.name = name_input


class ObjectsEngine:
    def __init__(self):
        self.objects_notation = dict()
        self.readiness = True

    def get_objects_notation(self, mouse_up: bool, mouse_pos: tuple):
        if mouse_up:
            temp_point = Point(mouse_pos[0], mouse_pos[1])
            self.__add__(SomeObject(f'Circle'), temp_point)

        if self.objects_notation != dict():
            temp_object_coordinates = self.objects_notation['Circle']

            if math.sqrt((temp_object_coordinates.x - mouse_pos[0]) ** 2 + (
                    temp_object_coordinates.y - mouse_pos[1]) ** 2) < 100 and self.readiness is True:
                self.__add__(SomeObject('Square'), Point(250, 250))
                self.readiness = False

            if math.sqrt((temp_object_coordinates.x - mouse_pos[0]) ** 2 + (
                    temp_object_coordinates.y - mouse_pos[1]) ** 2) > 100 and self.readiness is False:
                self.remove('Square')
                self.readiness = True

        return self.objects_notation

    def __add__(self, input_object: SomeObject, object_coordinates: Point):
        self.objects_notation.update({input_object.name: object_coordinates})

    def remove(self, input_object: SomeObject):
        self.objects_notation.pop(input_object)
