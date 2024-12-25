from engines.DrawingEngine import *
from engines.ObjectEngine import *

DRAWING_WINDOW_WIDTH = 900
DRAWING_WINDOW_HEIGHT = 900


class GameEngine:

    def __init__(self, demo_request_input: str):
        self.demo_name = demo_request_input

    def run(self):

        # 2. pygame setup
        pygame.init()

        # 3. window setup
        screen = pygame.display.set_mode((DRAWING_WINDOW_WIDTH, DRAWING_WINDOW_HEIGHT))

        # 3.1 Remove cursor on window frame
        pygame.mouse.set_visible(True)

        # 4. window name and icon setup
        program_icon = pygame.image.load('extras/icon.png')
        pygame.display.set_icon(program_icon)

        # 5. condition of running setup
        clock = pygame.time.Clock()

        # COEFFICIENT FOR DRAWING
        game_field_coef = 15

        # SEGMENTS COUNT
        sector_quantity = 10

        # 6. FPS init
        clock.tick()
        count = 0
        dt_list = []

        # 7. Condition of run init
        running = 1

        # 8. Objects engine init
        oe = ObjectsEngine(DRAWING_WINDOW_WIDTH, DRAWING_WINDOW_HEIGHT, game_field_coef, sector_quantity)

        # 9. Drawing engine init
        de = DrawingEngine(game_field_coef)

        # 8.3 interrupter declaration
        mouse_up = False
        mouse_down = False
        kb_space = False

        dt = 0

        # 9. Main loop
        while running:

            keys = pygame.key.get_pressed()

            # condition check to quit application
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = 0
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_up = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True
                elif event.type == pygame.KEYUP and pygame:
                    mouse_down = True

            if keys[pygame.K_SPACE]:
                kb_space = True

            mouse_pos = pygame.mouse.get_pos()

            screen.fill(COLOR_BLACK)

            pixel_array = pygame.PixelArray(screen)

            oe.update_set_of_objects((mouse_pos[0] * game_field_coef, mouse_pos[1] * game_field_coef),
                                     mouse_up,
                                     mouse_down,
                                     kb_space,
                                     self.demo_name,
                                     dt)

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
            kb_space = False
