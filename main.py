import settings.resolution
from engines.DrawingEngine import *
from engines.ObjectEngine import *
import pygame


def main():
    # 1. resolution setup
    WIDTH = settings.resolution.width
    HEIGHT = settings.resolution.height

    # 2. pygame setup
    pygame.init()

    # 3. window setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # 4. window name and icon setup
    program_icon = pygame.image.load('extras/icon.png')
    pygame.display.set_icon(program_icon)

    # 5. condition of running setup
    clock = pygame.time.Clock()

    # 6. FPS init
    clock.tick()
    count = 0
    dt_list = []

    # 7. Condition of run init
    running = 1

    # 8. Objects engine init
    oe = ObjectsEngine()

    # 9. Drawing engine init
    de = DrawingEngine()

    # #########################
    # STATIC OBJECT ADD HERE
    # #########################

    # 8.1 Static objects declaration - TEST FUNCTION
    objects_buffer = []

    for _ in range(5):
        dot1 = Dot(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        dot2 = Dot(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        i_circ = InteractiveCircle(i_dot=dot1, i_radius=30, i_color=COLOR_WHITE)
        i_circ2 = InteractiveCircle(i_dot=dot2, i_radius=30, i_color=COLOR_WHITE)
        i_line = Line(dot1, dot2, COLOR_WHITE, True, COLOR_RED, COLOR_RED)
        objects_buffer.append(i_circ)
        objects_buffer.append(i_circ2)
        objects_buffer.append(i_line)

    # 8.2 Test objects transferred to objects engine
    for pos in objects_buffer:
        oe.add_object(pos)

    # ###########################
    # END
    # ###########################

    # 8.3 interuptors declaration
    mouse_up = False
    mouse_down = False

    # 9. Main loop
    while running:

        # condition check to quit application
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_up = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        mouse_pos = pygame.mouse.get_pos()

        pixel_array = pygame.PixelArray(screen)

        screen.fill(COLOR_BLACK)

        oe.update_set_of_objects(mouse_pos, mouse_up, mouse_down, count)

        de.draw_window(pixel_array, oe.get_set_of_objects())

        pixel_array.close()

        pygame.display.flip()

        dt_list += [clock.tick()]
        if len(dt_list) > 100:
            del dt_list[0]
        if count % 100 == 0:
            dt_sum = sum(dt_list)
            if dt_sum > 0:
                pygame.display.set_caption("FPS: " + str(round(len(dt_list) / sum(dt_list) * 1000)))
        count += 1

        mouse_up = False
        mouse_down = False


if __name__ == '__main__':
    main()
