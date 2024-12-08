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

    PixelMatrixPM = PixelMatrix(WIDTH, HEIGHT)

    while running:

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        #  reset screen - so fill it black
        screen.fill(COLOR_BLACK)

        draw_window(PixelMatrixPM)

        for pos in PixelMatrixPM:
            if 0 < pos.x < WIDTH and 0 < pos.y < HEIGHT:
                screen.set_at((pos.x, pos.y), pos.color)

        pygame.display.flip()

        # frames per sec drawing
        clock.tick(120)

        PixelMatrixPM.clearMatrix()


def draw_window(input_pm: PixelMatrix):
    # p0 = Point(*toDecardCoordinates(random.randint(-100, 100), random.randint(-100, 100)))
    # p1 = Point(*toDecardCoordinates(random.randint(-100, 100), random.randint(-100, 100)))
    # draw_line(p0, p1, pixel_matrix, COLOR_GREEN, True, COLOR_RED, COLOR_RED)

    # p0 = Point(*toDecardCoordinates(0, 0))
    # p0 = Point(510, 510)

    radius = 15

    p1 = Point(50, 50)
    p2 = Point(250, 250)

    draw_circle(p1, radius, input_pm)
    draw_circle(p2, radius, input_pm)
    draw_line(p1, p2, input_pm)

    if pygame.mouse.get_focused():
        # x, y = pygame.mouse.get_pos()
        p0 = Point(*pygame.mouse.get_pos())
        draw_circle(p0, radius, input_pm)

        draw_line(p0, p1, input_pm)

        draw_line(p0, p2, input_pm)

        # p0 = Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        # draw_circle(p0, random.randint(10, 50), input_pm,
        #             (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        # p0 = Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        # p1 = Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        # p2 = Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        # draw_line(p0, p1, input_pm)
        # draw_line(p1, p2, input_pm)
        # draw_line(p2, p0, input_pm)


if __name__ == '__main__':
    main()
