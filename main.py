import random
import pygame
from drawing_functions import *
from additional_types import *
from drawing_engine import draw_window
import time
import math

WIDTH = settings.width
HEIGHT = settings.height


def main():
    # window setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # surface = pygame.surface

    # window name and icon setup
    pygame.display.set_caption('Graphics Module')
    program_icon = pygame.image.load('extras/icon.png')
    pygame.display.set_icon(program_icon)

    # condition of running setup
    clock = pygame.time.Clock()

    clock.tick()
    count = 0
    dt_list = []

    running = True

    # drawing engine init (cache init, borders init)
    pixel_matrix = PixelMatrix(WIDTH, HEIGHT)

    # main loop
    while running:
        # TEMP FEATURE
        pixel_array = pygame.PixelArray(screen)

        rect = pygame.Rect(screen.get_rect().center, (0, 0)).inflate(*([min(screen.get_size()) // 2] * 2))

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        #  reset screen - so fill it black
        # start = time.perf_counter()
        screen.fill(COLOR_BLACK)
        # end = time.perf_counter()
        # t1 = int((end - start) * 1000) / 1000

        # calculate exact pixels, which needs to be displayed
        # start = time.perf_counter()
        draw_window(pixel_matrix)
        # end = time.perf_counter()
        # t2 = int((end - start) * 1000) / 1000

        # draw pixels, stored in PixelMatrix
        # start = time.perf_counter()
        for coordinates, color in pixel_matrix:
            # screen.set_at((coordinates[0], coordinates[1]), color)
            # print(pygame.PixelArray.surface)
            # print(coordinates[0], coordinates[1])
            pixel_array[coordinates[0] - 1, coordinates[1] - 1] = color
        # end = time.perf_counter()
        # t3 = int((end - start) * 1000) / 1000

        pixel_array.close()

        # draw screen (full)
        # start = time.perf_counter()
        pygame.display.flip()
        # end = time.perf_counter()
        # t4 = int((end - start) * 1000) / 1000

        # wait time to synchronize to FPS
        # start = time.perf_counter()
        # clock.tick(120)
        # end = time.perf_counter()
        # t5 = int((end - start) * 1000) / 1000

        # print(t1, t2, t3, t4, t5, len(pixel_matrix))

        # clear PixelMatrix cache of used pixels
        # start = time.perf_counter()
        pixel_matrix.clear_matrix()
        # end = time.perf_counter()
        # t6 = int((end - start)*1000)/1000

        dt_list += [clock.tick()]
        if len(dt_list) > 100:
            del dt_list[0]
        if (count % 100 == 0):
            dt_sum = sum(dt_list)
            if dt_sum > 0:
                pygame.display.set_caption("FPS: " + str(round(len(dt_list) / sum(dt_list) * 1000)))
        count += 1


if __name__ == '__main__':
    main()
