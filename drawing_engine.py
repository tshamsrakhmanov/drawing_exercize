from drawing_functions import *
import pygame


def draw_window(pixel_array: pygame.pixelarray):
    def adjustable_triangle():

        radius = 15

        p1 = Point(50, 50)
        p2 = Point(250, 250)
        p3 = Point(350, 100)

        draw_circle(p1, radius, pixel_array, COLOR_RED)
        draw_circle(p2, radius, pixel_array, COLOR_RED)
        draw_circle(p3, radius, pixel_array, COLOR_RED)
        draw_line(p1, p2, pixel_array, COLOR_RED)
        draw_line(p2, p3, pixel_array, COLOR_RED)
        draw_line(p1, p3, pixel_array, COLOR_RED)

        if pygame.mouse.get_focused():
            p0 = Point(*pygame.mouse.get_pos())
            draw_circle(p0, radius, pixel_array, COLOR_WHITE)
            draw_line(p0, p1, pixel_array, COLOR_WHITE)
            draw_line(p0, p2, pixel_array, COLOR_WHITE)
            draw_line(p0, p3, pixel_array, COLOR_WHITE)

    def random_lines(count):
        for _ in range(count):
            draw_line(Point(random.randint(10, pixel_array.surface.get_size()[0] - 11),
                            random.randint(10, pixel_array.surface.get_size()[1] - 11)),
                      Point(random.randint(10, pixel_array.surface.get_size()[0] - 11),
                            random.randint(10, pixel_array.surface.get_size()[1] - 11)), pixel_array, COLOR_BLUE, True,
                      COLOR_RANDOM(), COLOR_RANDOM())

    def random_circles(count):
        for _ in range(count):
            p0 = Point(random.randint(75, pixel_array.surface.get_size()[0] - 76),
                       random.randint(75, pixel_array.surface.get_size()[1] - 76))
            draw_circle(p0, random.randint(3, 73), pixel_array, COLOR_RANDOM())

    def test_of_centerline_circle():
        p0 = Point(200, 200)
        draw_circle_centerline(p0, 40, pixel_array, COLOR_RED)

    def random_full_circles(count):

        min_radius = 5
        max_radius = 75
        gap = 1

        for _ in range(count):
            p0 = Point(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                       random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))
            draw_circle_centerline(p0, random.randint(min_radius, max_radius), pixel_array, COLOR_RANDOM())

    def triplets(count):
        def triplets_generation():
            min_radius = 5
            max_radius = 75
            gap = 1

            p0 = Point(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                       random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))
            p1 = Point(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                       random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))
            p2 = Point(random.randint(max_radius + gap, pixel_array.surface.get_size()[0] - (max_radius + gap)),
                       random.randint(max_radius + gap, pixel_array.surface.get_size()[1] - (max_radius + gap)))

            draw_circle_centerline(p0, random.randint(min_radius, max_radius), pixel_array, COLOR_WHITE)
            draw_circle_centerline(p1, random.randint(min_radius, max_radius), pixel_array, COLOR_WHITE)
            draw_circle_centerline(p2, random.randint(min_radius, max_radius), pixel_array, COLOR_WHITE)
            draw_line(p0, p1, pixel_array, COLOR_GREEN)
            draw_line(p1, p2, pixel_array, COLOR_GREEN)
            draw_line(p2, p0, pixel_array, COLOR_GREEN)

        for _ in range(count):
            triplets_generation()

    # adjustable_triangle()
    random_lines(100)
    # random_circles(100)
    # test_of_centerline_circle()
    # random_full_circles(300)
    # triplets(15)
