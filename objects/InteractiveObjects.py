from objects.GeometryObjects import *


class InteractiveObject:
    pass


class InteractiveCircle(Circle, InteractiveObject):
    def __init__(self, **kwargs):
        Circle.__init__(self, **kwargs)
        self.state = False

    def __repr__(self):
        return f'{str(self.__hash__())[-4:]} {'0' if self.state else '1'}'


class InteractiveDot(InteractiveObject):
    pass
