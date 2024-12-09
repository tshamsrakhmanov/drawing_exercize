import random
import pygame
from functions import *
from additional_types import *
from drawing_engine import draw_window
import time
import math

WIDTH = settings.width
HEIGHT = settings.height


def main():
    # window setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # window name and icon setup
    pygame.display.set_caption('Graphics Module')
    program_icon = pygame.image.load('extras/icon.png')
    pygame.display.set_icon(program_icon)

    # condition of running setup
    clock = pygame.time.Clock()
    running = True

    # drawing engine init (cache init, borders init)
    pixel_matrix = PixelMatrix(WIDTH, HEIGHT)

    # main loop
    while running:

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        #  reset screen - so fill it black
        screen.fill(COLOR_BLACK)

        # calculate exact pixels, which needs to be displayed
        draw_window(pixel_matrix)

        # draw pixels, stored in PixelMatrix
        for coordinates, color in pixel_matrix:
            screen.set_at((coordinates[0], coordinates[1]), color)

        # draw screen (full)
        pygame.display.flip()

        # wait time to synchronize to FPS
        clock.tick(120)

        # clear PixelMatrix cache of used pixels
        pixel_matrix.clear_matrix()


if __name__ == '__main__':
    main()
