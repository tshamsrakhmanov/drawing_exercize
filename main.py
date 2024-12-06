import random
import pygame
from functions import *
from additional_types import *
import time
import math

WIDTH = settings.width
HEIGHT = settings.height


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    coordinate_mesh = [[(0, 0, 0) for y in range(HEIGHT)] for i in range(WIDTH)]

    imp = 0

    while running:

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        draw_screen(coordinate_mesh, imp)

        for i in range(WIDTH):
            for y in range(HEIGHT):
                screen.set_at((i, y), coordinate_mesh[i][y])

        pygame.display.flip()

        # time pass
        clock.tick(240)

        imp += 1

        if imp == 360:
            imp = 0


def draw_screen(matrix, imp):
    # reset screen - fill it with 0-es
    for i in range(WIDTH):
        for y in range(HEIGHT):
            matrix[i][y] = (0, 0, 0)

    angle = imp

    #  base
    p0 = Point(csx(0), csy(0))
    p1 = Point(csx(int(math.cos(math.radians(angle)) * 100)), csy(int(math.sin(math.radians(angle)) * 100)))

    p_rnd = Point(random.randint(0, WIDTH - 1), random.randint(0, WIDTH - 1))

    # add_circle(p0, 100, matrix, color=COLOR_GREEN)
    # add_line(p0, p1, matrix, color=COLOR_BLACK, pointed=True, color_start=COLOR_RED, color_end=COLOR_RED)
    # add_circle(p_rnd, random.randint(10, 100), matrix,
    #            color=random.choice((COLOR_BLUE, COLOR_WHITE, COLOR_GREEN, COLOR_RED)))
    add_circle(Point(0, 150), 100, matrix)


if __name__ == '__main__':
    main()
