import settings
from DrawingEngine import draw_window
from ObjectEngine import *
import pygame
import os


def main():
    pygame.init()
    # window setup
    screen = pygame.display.set_mode((settings.width, settings.height))
    # surface = pygame.surface

    # window name and icon setup
    # pygame.display.set_caption('Graphics Module')
    program_icon = pygame.image.load('extras/icon.png')
    pygame.display.set_icon(program_icon)

    # condition of running setup
    clock = pygame.time.Clock()

    clock.tick()
    count = 0
    dt_list = []

    running = 1

    objects_engine = ObjectsEngine()

    for _ in range(10):
        i_circ = InteractiveCircle(i_dot=Dot(random.randint(100, settings.width - 100),
                                             random.randint(100, settings.height - 100)), i_radius=30,
                                   i_color=COLOR_WHITE)
        objects_engine.add_object(i_circ)

    i_circ2 = Circle(i_dot=Dot(random.randint(100, settings.width - 100),
                                         random.randint(100, settings.height - 100)), i_radius=30,
                               i_color=COLOR_GREEN)
    objects_engine.add_object(i_circ2)

    mouse_up = False
    mouse_pos = ()


    # main loop
    while running:

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = 0

        mouse_pos = pygame.mouse.get_pos()

        pixel_array = pygame.PixelArray(screen)

        screen.fill(COLOR_BLACK)

        temp1 = objects_engine.objects_state(mouse_pos)

        draw_window(pixel_array, temp1)

        pixel_array.close()

        pygame.display.flip()

        dt_list += [clock.tick()]
        if len(dt_list) > 100:
            del dt_list[0]
        if (count % 100 == 0):
            dt_sum = sum(dt_list)
            if dt_sum > 0:
                pygame.display.set_caption("FPS: " + str(round(len(dt_list) / sum(dt_list) * 1000)))
        count += 1

        # resetting interruptors
        mouse_up = False


if __name__ == '__main__':
    main()
