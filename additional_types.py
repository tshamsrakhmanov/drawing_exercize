from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class RGBColor:
    r: int
    g: int
    b: int


@dataclass
class DrawablePixel:
    x: int
    y: int
    color: RGBColor


@dataclass
class PixelMatrix:
    internalStorage: list
    matrix_size_x: int
    matrix_size_y: int

    def addPixel(self, input_pixel: DrawablePixel):

        if 0 <= input_pixel.x <= self.matrix_size_x and 0 <= input_pixel.y <= self.matrix_size_y:
            self.internalStorage.append(input_pixel)

    def __init__(self, dimention_x, dimetion_y):

        if dimention_x > 0 and dimetion_y:
            self.matrix_size_x = dimention_x
            self.matrix_size_y = dimetion_y
            self.internalStorage = []
        else:
            raise ValueError('No value provided for screen resolution')

    def __iter__(self):
        return iter(self.internalStorage)

    def clearMatrix(self):
        self.internalStorage.clear()