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


class MovableCircle(Circle, InteractiveObject):

    def __init__(self, vector: Vector, **kwargs):
        Circle.__init__(self, **kwargs)
        self.vector = vector
        self.sector_x = None
        self.sector_y = None


class ChainPiece(Circle, InteractiveObject):
    def __init__(self, next_link: InteractiveObject or None, link_size: int, **kwargs):
        Circle.__init__(self, **kwargs)
        self.next_link = next_link
        self.link_size = link_size


class BezierPoint(InteractiveObject):

    def __init__(self, x, y, is_on_line: bool):
        self.coordinate_x = x
        self.coordinate_y = y
        self.is_on_line = is_on_line

    def __repr__(self):
        return f'BezierPoint ({self.coordinate_x},{self.coordinate_y}) ({"X" if self.is_on_line else "V"})'


class BezierContainer(InteractiveObject):

    def __init__(self, *args: BezierPoint):
        self.list_of_bezier_points = list(args)

    def __iter__(self):
        return iter(self.list_of_bezier_points)

    def __repr__(self):
        return f'BezierContainer {[str(i) for i in self.list_of_bezier_points]}'

    def __len__(self):
        return len(self.list_of_bezier_points)
