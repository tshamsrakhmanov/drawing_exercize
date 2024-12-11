from objects.GeometryObjects import *


class InteractiveObject:
    pass


class PinBoardCircle(Circle, InteractiveObject):
    focus_color = COLOR_ORANGE
    base_color = COLOR_WHITE

    color_active_focused = focus_color
    color_active_non_focused = base_color
    color_non_active_focused = focus_color
    color_non_active_non_focused = base_color

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        self.active = False  # ACTIVE | NON-ACTIVE
        self.focus_non_active_ready = True
        self.focus_active_ready = True
        self.movable = True


class GradientCircle(Circle, InteractiveObject):

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        self.actual_size = 0


class Vector(InteractiveObject):

    def __init__(self, degree: float, dot_input: Dot, energy_input: float = 100.0):
        self.degree = degree
        self.dot = dot_input
        self.energy = energy_input

        # def __repr__(self):
    #     return f'{self.dot} {self.normal_x} {self.normal_y}'


class MovableCircle(Circle, InteractiveObject):

    def __init__(self, vector: Vector, **kwargs):
        Circle.__init__(self, **kwargs)
        self.vector = vector
        self.sector = None
