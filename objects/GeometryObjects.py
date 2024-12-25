from settings.colors import *

class Dot:
    def __init__(self, i_x, i_y, i_color: RGBColor = COLOR_WHITE):
        self.i_color = i_color
        self.coordinate_x = i_x
        self.coordinate_y = i_y

    def __repr__(self):
        return f'Dot({self.coordinate_x},{self.coordinate_y})'


class Line:
    def __init__(self, i_dot1: Dot, i_dot2: Dot, i_color: RGBColor, is_pointed: bool, color_point_start: RGBColor,
                 color_point_end=RGBColor):
        self.i_color = i_color
        self.dot_start = i_dot1
        self.dot_end = i_dot2
        self.color = i_color
        self.is_pointed = is_pointed
        self.color_point_start = color_point_start
        self.color_point_end = color_point_end

    def __repr__(self):
        return f'Line({self.dot_start.coordinate_x},{self.dot_start.coordinate_y} - {self.dot_end.coordinate_x},{self.dot_end.coordinate_y})'


class Circle():
    def __init__(self, i_dot: Dot, i_radius: int, i_color:RGBColor):
        self.i_color = i_color
        self.center_point = i_dot
        self.radius = i_radius

    def __repr__(self):
        return f'Cicrle({self.center_point.coordinate_x},{self.center_point.coordinate_y} - {self.radius} - {self.color})'
