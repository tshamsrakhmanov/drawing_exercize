import settings
from additional_types import *
from colors import *


def csx(x):
    return int(settings.width / 2) + x


def csy(y):
    return int(settings.height / 2) - y


def add_circle(point: Point, radius, matrix, color=(255, 255, 255)):

    for dx in range(radius):
        for dy in range(radius):
            if dx ** 2 + dy ** 2 <= radius ** 2:
                try:
                    matrix[dx + point.x][dy + point.y] = color

                except Exception:
                    pass
                try:
                    matrix[dx + point.x][-dy + point.y] = color
                except Exception:
                    pass
                try:
                    matrix[-dx + point.x][dy + point.y] = color
                except Exception:
                    pass
                try:
                    matrix[-dx + point.x][-dy + point.y] = color
                except Exception:
                    pass





def add_point(point: Point, matrix, color=(255, 255, 255)):
    try:
        matrix[point.x + 1][point.y] = color
        matrix[point.x - 1][point.y] = color
        matrix[point.x][point.y] = color
        matrix[point.x][point.y - 1] = color
        matrix[point.x][point.y + 1] = color
    except Exception:
        pass


def add_line(point_start: Point, point_end: Point, matrix, color=COLOR_WHITE, pointed=False, color_start=COLOR_WHITE,
             color_end=COLOR_WHITE):
    # Implementation line-by-line of algorythm declared in article:
    # https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

    x0 = point_start.x
    x1 = point_end.x
    y0 = point_start.y
    y1 = point_end.y

    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -1 * abs(y1 - y0)
    sy = 1 if y0 < y1 else -1

    error = dx + dy

    while True:
        try:
            matrix[x0][y0] = color
        except Exception:
            pass
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * error
        if e2 >= dy:
            error += dy
            x0 += sx
        if e2 <= dx:
            error += dx
            y0 += sy

    if pointed:
        add_point(point_start, matrix, color_start)
        add_point(point_end, matrix, color_end)
