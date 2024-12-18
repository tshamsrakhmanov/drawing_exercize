from engines.DrawingEngine import *
from engines.ObjectEngine import *
WIDTH = 900
HEIGHT = 900


class GameEngine:

    def __init__(self, demo_request_input: str):
        self.demo = demo_request_input

    def run(self):

        # 2. pygame setup
        pygame.init()

        # 3. window setup
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # 3.1 Remove cursor on window frame
        pygame.mouse.set_visible(True)

        # 4. window name and icon setup
        program_icon = pygame.image.load('extras/icon.png')
        pygame.display.set_icon(program_icon)

        # 5. condition of running setup
        clock = pygame.time.Clock()

        # COEFFICIENT FOR DRAWING
        coef = 15

        # SEGMENTS COUNT
        sector_quantity = 10

        # 6. FPS init
        clock.tick()
        count = 0
        fps = 0
        dt_list = []

        # 7. Condition of run init
        running = 1

        # 8. Objects engine init
        oe = ObjectsEngine(WIDTH, HEIGHT, coef, sector_quantity)

        # 9. Drawing engine init
        de = DrawingEngine(coef)

        # 8.1 Static objects declaration - TEST FUNCTION
        objects_buffer = []

        if self.demo is None:
            raise Exception('No demo requested')
        elif self.demo == 'triangle':
            self.demo_triangle(objects_buffer, (coef * WIDTH, coef * HEIGHT))
        elif self.demo == 'gradient':
            self.demo_gradient(objects_buffer)
        elif self.demo == 'sandbox':
            self.demo_sandbox(objects_buffer)

        # 8.2 Test objects transferred to objects engine
        for pos in objects_buffer:
            oe.add_object(pos)

        # 8.3 interuptors declaration
        mouse_up = False
        mouse_down = False

        dt = 0

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

            oe.update_set_of_objects((mouse_pos[0] * coef, mouse_pos[1] * coef), mouse_up, mouse_down, dt)

            de.draw_window(pixel_array, oe.get_set_of_objects())

            pixel_array.close()

            pygame.display.flip()

            dt = clock.tick(60)
            dt_list += [dt]
            if len(dt_list) > 100:
                del dt_list[0]
            if count % 100 == 0:
                dt_sum = sum(dt_list)
                if dt_sum > 0:
                    fps = round(len(dt_list) / sum(dt_list) * 1000)
                    pygame.display.set_caption("FPS: " + str(fps))
            count += 1

            mouse_up = False
            mouse_down = False

    @staticmethod
    def demo_triangle(input_buffer, game_field):
        for _ in range(1):
            dot1 = Dot(game_field[0] / 2, game_field[1] / 4)
            dot2 = Dot(math.floor(game_field[0] * 3 / 4), math.floor(game_field[1] * 3 / 4))
            dot3 = Dot(math.floor(game_field[0] * 1 / 4), math.floor(game_field[1] * 3 / 4))
            i_circ1 = PinBoardCircle(i_dot=dot1, i_radius=150, i_color=COLOR_WHITE)
            i_circ2 = PinBoardCircle(i_dot=dot2, i_radius=150, i_color=COLOR_WHITE)
            i_circ3 = PinBoardCircle(i_dot=dot3, i_radius=150, i_color=COLOR_WHITE)
            i_line1 = Line(dot1, dot2, COLOR_RED, False, COLOR_RED, COLOR_RED)
            i_line2 = Line(dot2, dot3, COLOR_GREEN, False, COLOR_RED, COLOR_RED)
            i_line3 = Line(dot1, dot3, COLOR_BLUE, False, COLOR_RED, COLOR_RED)
            input_buffer.append(i_circ1)
            input_buffer.append(i_circ2)
            input_buffer.append(i_circ3)
            input_buffer.append(i_line1)
            input_buffer.append(i_line2)
            input_buffer.append(i_line3)

    @staticmethod
    def demo_gradient(input_buffer):
        distance = 40

        for i in range(5, 38):  # 38
            for y in range(1, 19):  # 19
                temp_dot = Dot(distance * i, distance * y)
                input_buffer.append(
                    GradientCircle(i_dot=temp_dot, i_radius=10, i_color=COLOR_WHITE))

    @staticmethod
    def demo_sandbox(input_buffer):
        pass
