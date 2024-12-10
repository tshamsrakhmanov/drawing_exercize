from objects.GeometryObjects import *


class InteractiveObject:
    pass


class InteractiveCircle(Circle, InteractiveObject):
    focus_color = COLOR_ORANGE
    base_color = COLOR_WHITE

    color_active_focused = focus_color
    color_active_non_focused = base_color
    color_non_active_focused = focus_color
    color_non_active_non_focused = base_color

    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        self.active = True  # ACTIVE | NON-ACTIVE
        self.focus_non_active_ready = True
        self.focus_active_ready = True

    def __repr__(self):
        return f'{str(self.__hash__())[-4:]} {'0' if self.active else '1'}'


class InteractiveDot(InteractiveObject):
    pass
