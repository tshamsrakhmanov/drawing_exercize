import random


class RGBColor:
    r: int
    g: int
    b: int


COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ORANGE = (255, 255, 0)
COLOR_TEAL = (0, 128, 128)
COLOR_GREY = (100, 100, 100)
COLOR_YELLOW = (255, 255, 0)


def COLOR_RANDOM():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
