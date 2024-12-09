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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption('Graphics Module')
    programIcon = pygame.image.load('extras/icon.png')
    pygame.display.set_icon(programIcon)

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

        # print(PixelMatrixPM)

        for coordinates, color in PixelMatrixPM:
            screen.set_at((coordinates[0], coordinates[1]), color)

        pygame.display.flip()

        # frames per sec drawing
        clock.tick(120)

        PixelMatrixPM.clear_matrix()


if __name__ == '__main__':
    main()
