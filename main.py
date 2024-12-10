import settings.resolution
from engines.DrawingEngine import *
from engines.ObjectEngine import *
import pygame
import argparse

WIDTH = settings.resolution.width
HEIGHT = settings.resolution.height


def main(demo_type):
    # 1. resolution setup

    # 2. pygame setup
    pygame.init()

    # 3. window setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.mouse.set_visible(False)

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

    if demo_type is None:
        raise Exception('No demo requested')
    elif demo_type == 'triangle':
        demo_triangle(objects_buffer)
    elif demo_type == 'gradient':
        demo_gradient(objects_buffer)

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

        oe.update_set_of_objects(mouse_pos, mouse_up, mouse_down)

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


def demo_triangle(input_buffer):
    for _ in range(1):
        dot1 = Dot(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        dot2 = Dot(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        dot3 = Dot(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        dot4 = Dot(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
        i_circ1 = MovableCircle(i_dot=dot1, i_radius=15, i_color=COLOR_WHITE)
        i_circ2 = MovableCircle(i_dot=dot2, i_radius=15, i_color=COLOR_WHITE)
        i_circ3 = MovableCircle(i_dot=dot3, i_radius=15, i_color=COLOR_WHITE)
        i_line1 = Line(dot1, dot2, COLOR_RED, False, COLOR_RED, COLOR_RED)
        i_line2 = Line(dot2, dot3, COLOR_GREEN, False, COLOR_RED, COLOR_RED)
        i_line3 = Line(dot1, dot3, COLOR_BLUE, False, COLOR_RED, COLOR_RED)
        input_buffer.append(i_circ1)
        input_buffer.append(i_circ2)
        input_buffer.append(i_circ3)
        input_buffer.append(i_line1)
        input_buffer.append(i_line2)
        input_buffer.append(i_line3)


def demo_gradient(input_buffer):
    distance = 40

    for i in range(5, 38):  # 38
        for y in range(1, 19):  # 19
            temp_dot = Dot(distance * i, distance * y)
            input_buffer.append(
                GradientCircle(i_dot=temp_dot, i_radius=10, i_color=COLOR_WHITE))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Some parser')
    parser.add_argument('--type', type=str, help='type of demo to show')
    args = parser.parse_args()

    main(args.type)
