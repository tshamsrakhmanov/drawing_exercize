import settings
from additional_types import *
from colors import *


def draw_circle(point: Point, radius, matrix, color=(255, 255, 255)):
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


def draw_point(
        input_point: Point,
        input_pixel_mesh: list,
        input_color: RGBColor = (255, 255, 255)):
    input_pixel_mesh.append(DrawablePixel(input_point.x + 1, input_point.y, input_color))
    input_pixel_mesh.append(DrawablePixel(input_point.x - 1, input_point.y, input_color))
    input_pixel_mesh.append(DrawablePixel(input_point.x, input_point.y, input_color))
    input_pixel_mesh.append(DrawablePixel(input_point.x, input_point.y - 1, input_color))
    input_pixel_mesh.append(DrawablePixel(input_point.x, input_point.y + 1, input_color))


def draw_line(point_start: Point,
              point_end: Point,
              input_pixel_mesh: list,
              color_of_line: RGBColor = COLOR_WHITE,
              pointed=False,
              color_start: RGBColor = COLOR_WHITE,
              color_end: RGBColor = COLOR_WHITE):
    # Implementation line-by-line of algorythm declared in article:
    # https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    # some ohter comment

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
        input_pixel_mesh.append(DrawablePixel(x0, y0, color_of_line))

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
        draw_point(point_start, input_pixel_mesh, color_start)
        draw_point(point_end, input_pixel_mesh, color_end)


def toDecardCoordinates(x_input: int, y_input: int):
    return int(settings.width / 2) + x_input, int(settings.height / 2) - y_input
