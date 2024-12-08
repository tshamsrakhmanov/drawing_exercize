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

    while running:

        coordinate_mesh = []

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        #  reset screen - so fill it black
        screen.fill(COLOR_BLACK)

        draw_window(coordinate_mesh)

        for pos in coordinate_mesh:
            if 0 < pos.x < WIDTH and 0 < pos.y < HEIGHT:
                screen.set_at((pos.x, pos.y), pos.color)

        pygame.display.flip()

        # frames per sec drawing
        clock.tick(120)


def draw_window(coordinate_mesh):
    p0 = Point(*toDecardCoordinates(random.randint(-100, 100), random.randint(-100, 100)))
    p1 = Point(*toDecardCoordinates(random.randint(-100, 100), random.randint(-100, 100)))
    draw_line(p0, p1, coordinate_mesh, COLOR_GREEN, True, COLOR_RED, COLOR_RED)


if __name__ == '__main__':
    main()
