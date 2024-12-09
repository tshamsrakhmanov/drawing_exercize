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
    internalStorage: dict
    matrix_size_x: int
    matrix_size_y: int

    def add_pixel(self, input_pixel: DrawablePixel):
        if 0 <= input_pixel.x <= self.matrix_size_x and 0 <= input_pixel.y <= self.matrix_size_y:
            self.internalStorage.setdefault((input_pixel.x, input_pixel.y), input_pixel.color)

    def __init__(self, dimension_x, dimesion_y):

        if dimension_x > 0 and dimesion_y:
            self.matrix_size_x = dimension_x
            self.matrix_size_y = dimesion_y
            self.internalStorage = dict()
        else:
            raise ValueError('No value provided for screen resolution')

    def __iter__(self):
        return iter(self.internalStorage.items())

    def clear_matrix(self):
        self.internalStorage.clear()
