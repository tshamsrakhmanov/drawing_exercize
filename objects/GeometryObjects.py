from settings.colors import *


class Geometry:
    def __init__(self, i_color: RGBColor = COLOR_WHITE):
        self.color = i_color


class Dot(Geometry):
    def __init__(self, i_x, i_y, i_color: RGBColor = COLOR_WHITE):
        super().__init__(i_color)
        self.x = i_x
        self.y = i_y

    def __repr__(self):
        return f'Dot({self.x},{self.y})'


class Line(Geometry):
    def __init__(self, i_dot1: Dot, i_dot2: Dot, i_color: RGBColor, is_pointed: bool, color_point_start: RGBColor,
                 color_point_end=RGBColor):
        super().__init__(i_color)
        self.dot_start = i_dot1
        self.dot_end = i_dot2
        self.color = i_color
        self.is_pointed = is_pointed
        self.color_point_start = color_point_start
        self.color_point_end = color_point_end

    def __repr__(self):
        return f'Line({self.dot_start.x},{self.dot_start.y} - {self.dot_end.x},{self.dot_end.y})'


class Circle(Geometry):
    def __init__(self, i_dot: Dot, i_radius: int, **kwargs):
        super().__init__(**kwargs)
        self.dot_start = i_dot
        self.radius = i_radius

    def __repr__(self):
        return f'Cicrle({self.dot_start.x},{self.dot_start.y} - {self.radius} - {self.color})'
