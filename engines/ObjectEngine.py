import math
from objects.InteractiveObjects import PinBoardCircle, GradientCircle, MovableCircle, Vector, Line, ChainPiece, \
    BezierPoint, BezierContainer
from objects.GeometryObjects import Dot
from settings.colors import *


class ObjectsEngine:
    # to resolve out-of bounds movement

    def __init__(self, width: int, height: int, coef: int, segments: int):

        self.set_of_objects = set()
        self.ticker_cache = None
        self.field_coordinate_x = width * coef
        self.field_coordinate_y = height * coef
        self.drawing_coef = coef
        self.energy_loss = 0.95
        self.boundary_for_moving_objects = 500
        self.sectoring_factor = segments
        self.segment_dimension_x = int(self.field_coordinate_x / self.sectoring_factor)
        self.segment_dimension_y = int(self.field_coordinate_x / self.sectoring_factor)
        self.timer = 0
        self.time_previous = 0
        self.started = False

    def get_objects_by_adjacent_sector(self, sector_id_x_input: int, sector_id_y_input, obj_self):

        return set(filter(lambda x:
                          isinstance(x, MovableCircle) and
                          x.sector_x - 1 <= sector_id_x_input <= x.sector_x + 1 and
                          x.sector_y - 1 <= sector_id_y_input <= x.sector_y + 1 and
                          x != obj_self, self.set_of_objects))

    def update_set_of_objects(self, mouse_pos: tuple, mouse_up: bool, mouse_down: bool, kb_space: bool, demo_name: str,
                              dt: int):

        # Reset scene by space keyboard invoke - available each 1000 secs
        self.timer += dt

        ###############################################
        # INITIAL GAME SETUP - ADD OBJECTS BY DEMO NAME
        ###############################################

        if kb_space and not self.started:
            self.started = True
            if demo_name == 'sample_collisions':
                self.set_of_objects.clear()

                sectors_quantity = 5

                for i in range(sectors_quantity):
                    temp_dot = Dot((mouse_pos[0]) + random.randint(-500, 500),
                                   (mouse_pos[1]) + random.randint(-500, 500))
                    vector_1 = Vector(float(360 * i / sectors_quantity) + 14, temp_dot,
                                      energy_input=float(random.randint(1500, 3000)))
                    movable_circle = MovableCircle(vector_1, i_dot=temp_dot, i_radius=random.randint(5, 25),
                                                   i_color=COLOR_RANDOM())

                    dot_tail1 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail2 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail3 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail4 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail5 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail6 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail7 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail8 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail9 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail10 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail11 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail12 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail13 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail14 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail15 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail16 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail17 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail18 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail19 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)
                    dot_tail20 = Dot(temp_dot.coordinate_x, temp_dot.coordinate_y)

                    sneak_tail1 = ChainPiece(movable_circle, link_size=29, i_dot=dot_tail1, i_radius=30,
                                             i_color=(255, 0, 0))
                    sneak_tail2 = ChainPiece(sneak_tail1, link_size=28, i_dot=dot_tail2, i_radius=30,
                                             i_color=(255, 40, 0))
                    sneak_tail3 = ChainPiece(sneak_tail2, link_size=27, i_dot=dot_tail3, i_radius=30,
                                             i_color=(255, 80, 0))
                    sneak_tail4 = ChainPiece(sneak_tail3, link_size=26, i_dot=dot_tail4, i_radius=30,
                                             i_color=(255, 140, 0))
                    sneak_tail5 = ChainPiece(sneak_tail4, link_size=25, i_dot=dot_tail5, i_radius=30,
                                             i_color=(255, 178, 0))
                    sneak_tail6 = ChainPiece(sneak_tail5, link_size=24, i_dot=dot_tail6, i_radius=30,
                                             i_color=(255, 216, 0))
                    sneak_tail7 = ChainPiece(sneak_tail6, link_size=23, i_dot=dot_tail7, i_radius=30,
                                             i_color=(255, 255, 0))
                    sneak_tail8 = ChainPiece(sneak_tail7, link_size=22, i_dot=dot_tail8, i_radius=30,
                                             i_color=(170, 216, 0))
                    sneak_tail9 = ChainPiece(sneak_tail8, link_size=21, i_dot=dot_tail9, i_radius=30,
                                             i_color=(85, 176, 0))
                    sneak_tail10 = ChainPiece(sneak_tail9, link_size=20, i_dot=dot_tail10, i_radius=30,
                                              i_color=(0, 140, 0))
                    sneak_tail11 = ChainPiece(sneak_tail10, link_size=19, i_dot=dot_tail11, i_radius=30,
                                              i_color=(0, 156, 85))
                    sneak_tail12 = ChainPiece(sneak_tail11, link_size=18, i_dot=dot_tail12, i_radius=30,
                                              i_color=(0, 173, 170))
                    sneak_tail13 = ChainPiece(sneak_tail12, link_size=17, i_dot=dot_tail13, i_radius=30,
                                              i_color=(0, 191, 255))
                    sneak_tail14 = ChainPiece(sneak_tail13, link_size=16, i_dot=dot_tail14, i_radius=30,
                                              i_color=(0, 127, 238))
                    sneak_tail15 = ChainPiece(sneak_tail14, link_size=15, i_dot=dot_tail15, i_radius=30,
                                              i_color=(0, 64, 221))
                    sneak_tail16 = ChainPiece(sneak_tail15, link_size=14, i_dot=dot_tail16, i_radius=30,
                                              i_color=(0, 0, 205))
                    sneak_tail17 = ChainPiece(sneak_tail16, link_size=13, i_dot=dot_tail17, i_radius=30,
                                              i_color=(46, 0, 183))
                    sneak_tail18 = ChainPiece(sneak_tail17, link_size=12, i_dot=dot_tail18, i_radius=30,
                                              i_color=(92, 0, 161))
                    sneak_tail19 = ChainPiece(sneak_tail18, link_size=11, i_dot=dot_tail19, i_radius=30,
                                              i_color=(140, 0, 140))
                    sneak_tail20 = ChainPiece(sneak_tail19, link_size=10, i_dot=dot_tail20, i_radius=30,
                                              i_color=(140, 0, 140))

                    self.add_object(sneak_tail1)
                    self.add_object(sneak_tail2)
                    self.add_object(sneak_tail3)
                    self.add_object(sneak_tail4)
                    self.add_object(sneak_tail5)
                    self.add_object(sneak_tail6)
                    self.add_object(sneak_tail7)
                    self.add_object(sneak_tail8)
                    self.add_object(sneak_tail9)
                    self.add_object(sneak_tail10)
                    self.add_object(sneak_tail11)
                    self.add_object(sneak_tail12)
                    self.add_object(sneak_tail13)
                    self.add_object(sneak_tail14)
                    self.add_object(sneak_tail15)
                    self.add_object(sneak_tail16)
                    self.add_object(sneak_tail17)
                    self.add_object(sneak_tail18)
                    self.add_object(sneak_tail19)
                    self.add_object(sneak_tail20)
                    self.add_object(movable_circle)
            elif demo_name == 'triangle':
                dot1 = Dot(self.field_coordinate_x / 2, self.field_coordinate_y / 4)
                dot2 = Dot(math.floor(self.field_coordinate_x * 3 / 4),
                           math.floor(self.field_coordinate_y * 3 / 4))
                dot3 = Dot(math.floor(self.field_coordinate_x * 1 / 4), math.floor(self.field_coordinate_y * 3 / 4))
                i_circ1 = PinBoardCircle(i_dot=dot1, i_radius=25, i_color=COLOR_WHITE)
                i_circ2 = PinBoardCircle(i_dot=dot2, i_radius=25, i_color=COLOR_WHITE)
                i_circ3 = PinBoardCircle(i_dot=dot3, i_radius=25, i_color=COLOR_WHITE)
                i_line1 = Line(dot1, dot2, COLOR_RED, False, COLOR_RED, COLOR_RED)
                i_line2 = Line(dot2, dot3, COLOR_GREEN, False, COLOR_RED, COLOR_RED)
                i_line3 = Line(dot1, dot3, COLOR_BLUE, False, COLOR_RED, COLOR_RED)
                self.add_object(i_circ1)
                self.add_object(i_circ2)
                self.add_object(i_circ3)
                self.add_object(i_line1)
                self.add_object(i_line2)
                self.add_object(i_line3)
            elif demo_name == 'gradient':
                distance = 40 * self.drawing_coef
                for i in range(1, 19):  # 38
                    for y in range(1, 19):  # 19
                        temp_dot = Dot(distance * i, distance * y)
                        self.add_object(GradientCircle(i_dot=temp_dot, i_radius=10, i_color=COLOR_WHITE))
            elif demo_name == 'link':

                dot_head = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail1 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail2 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail3 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail4 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail5 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail6 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail7 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail8 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail9 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail10 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail11 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail12 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail13 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail14 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail15 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail16 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail17 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail18 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail19 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)
                dot_tail20 = Dot(self.field_coordinate_x * 1 / 2, self.field_coordinate_y * 1 / 2)

                sneak_head = PinBoardCircle(i_dot=dot_head, i_radius=30, i_color=COLOR_WHITE)
                sneak_tail1 = ChainPiece(sneak_head, link_size=29, i_dot=dot_tail1, i_radius=30, i_color=(255, 0, 0))
                sneak_tail2 = ChainPiece(sneak_tail1, link_size=28, i_dot=dot_tail2, i_radius=30, i_color=(255, 40, 0))
                sneak_tail3 = ChainPiece(sneak_tail2, link_size=27, i_dot=dot_tail3, i_radius=30, i_color=(255, 80, 0))
                sneak_tail4 = ChainPiece(sneak_tail3, link_size=26, i_dot=dot_tail4, i_radius=30, i_color=(255, 140, 0))
                sneak_tail5 = ChainPiece(sneak_tail4, link_size=25, i_dot=dot_tail5, i_radius=30, i_color=(255, 178, 0))
                sneak_tail6 = ChainPiece(sneak_tail5, link_size=24, i_dot=dot_tail6, i_radius=30, i_color=(255, 216, 0))
                sneak_tail7 = ChainPiece(sneak_tail6, link_size=23, i_dot=dot_tail7, i_radius=30, i_color=(255, 255, 0))
                sneak_tail8 = ChainPiece(sneak_tail7, link_size=22, i_dot=dot_tail8, i_radius=30, i_color=(170, 216, 0))
                sneak_tail9 = ChainPiece(sneak_tail8, link_size=21, i_dot=dot_tail9, i_radius=30, i_color=(85, 176, 0))
                sneak_tail10 = ChainPiece(sneak_tail9, link_size=20, i_dot=dot_tail10, i_radius=30, i_color=(0, 140, 0))
                sneak_tail11 = ChainPiece(sneak_tail10, link_size=19, i_dot=dot_tail11, i_radius=30,
                                          i_color=(0, 156, 85))
                sneak_tail12 = ChainPiece(sneak_tail11, link_size=18, i_dot=dot_tail12, i_radius=30,
                                          i_color=(0, 173, 170))
                sneak_tail13 = ChainPiece(sneak_tail12, link_size=17, i_dot=dot_tail13, i_radius=30,
                                          i_color=(0, 191, 255))
                sneak_tail14 = ChainPiece(sneak_tail13, link_size=16, i_dot=dot_tail14, i_radius=30,
                                          i_color=(0, 127, 238))
                sneak_tail15 = ChainPiece(sneak_tail14, link_size=15, i_dot=dot_tail15, i_radius=30,
                                          i_color=(0, 64, 221))
                sneak_tail16 = ChainPiece(sneak_tail15, link_size=14, i_dot=dot_tail16, i_radius=30,
                                          i_color=(0, 0, 205))
                sneak_tail17 = ChainPiece(sneak_tail16, link_size=13, i_dot=dot_tail17, i_radius=30,
                                          i_color=(46, 0, 183))
                sneak_tail18 = ChainPiece(sneak_tail17, link_size=12, i_dot=dot_tail18, i_radius=30,
                                          i_color=(92, 0, 161))
                sneak_tail19 = ChainPiece(sneak_tail18, link_size=11, i_dot=dot_tail19, i_radius=30,
                                          i_color=(140, 0, 140))
                sneak_tail20 = ChainPiece(sneak_tail19, link_size=10, i_dot=dot_tail20, i_radius=30,
                                          i_color=(140, 0, 140))

                self.add_object(sneak_head)
                self.add_object(sneak_tail1)
                self.add_object(sneak_tail2)
                self.add_object(sneak_tail3)
                self.add_object(sneak_tail4)
                self.add_object(sneak_tail5)
                self.add_object(sneak_tail6)
                self.add_object(sneak_tail7)
                self.add_object(sneak_tail8)
                self.add_object(sneak_tail9)
                self.add_object(sneak_tail10)
                self.add_object(sneak_tail11)
                self.add_object(sneak_tail12)
                self.add_object(sneak_tail13)
                self.add_object(sneak_tail14)
                self.add_object(sneak_tail15)
                self.add_object(sneak_tail16)
                self.add_object(sneak_tail17)
                self.add_object(sneak_tail18)
                self.add_object(sneak_tail19)
                self.add_object(sneak_tail20)
            elif demo_name == 'bezier':
                dot1 = Dot(self.field_coordinate_x * 2 / 8, self.field_coordinate_y * 4 / 8)
                dot2 = Dot(self.field_coordinate_x / 2, self.field_coordinate_y / 2)
                dot3 = Dot(self.field_coordinate_x * 6 / 8, self.field_coordinate_y * 4 / 8)
                b1 = BezierPoint(dot1.coordinate_x, dot1.coordinate_y, True)
                b2 = BezierPoint(dot2.coordinate_x, dot2.coordinate_y, False)
                b3 = BezierPoint(dot3.coordinate_x, dot3.coordinate_y, True)
                bc1 = BezierContainer(b1, b2, b3)
                mv1 = PinBoardCircle(i_dot=b2, i_radius=25, i_color=COLOR_WHITE)
                self.add_object(bc1)
                self.add_object(mv1)

        ##########################################
        # OBJECTS LOOP - UPDATE STATE OF AN OBJECT
        ##########################################

        for obj in self.set_of_objects:

            if isinstance(obj, GradientCircle):

                """
                only for this respective dimensions:
                for i in range(1, 38): # 38
                    for y in range(1, 19): # 19
                        temp_dot = Dot(distance * i, distance * y)
                        objects_buffer.append(
                            GradientCircle(i_dot=temp_dot, i_radius=10, i_color=COLOR_WHITE))
                """

                distance = math.sqrt((mouse_pos[0] - obj.center_point.coordinate_x) ** 2 + (
                        mouse_pos[1] - obj.center_point.coordinate_y) ** 2)

                max_dist = 40 * self.drawing_coef
                min_dist = 1
                delta_dist = max_dist - min_dist

                if distance >= obj.radius * max_dist:
                    obj.actual_size = obj.radius * 2
                    obj.color = COLOR_GREEN
                elif obj.radius * min_dist <= distance < obj.radius * max_dist:
                    coefficient = (distance - min_dist * obj.radius) / (delta_dist * obj.radius)
                    obj.actual_size = int(
                        (obj.radius / 2) + (1.5 * obj.radius) * coefficient)
                    obj.color = (int(255 - 255 * coefficient), int(0 + 255 * coefficient), 0)
                else:
                    obj.actual_size = int(obj.radius / 4)
                    obj.color = COLOR_RED
            elif isinstance(obj, PinBoardCircle):

                distance = math.sqrt((mouse_pos[0] - obj.center_point.coordinate_x) ** 2 + (
                        mouse_pos[1] - obj.center_point.coordinate_y) ** 2)

                # Feature - focus light of active / inactive circle - p.1
                if distance < obj.radius * self.drawing_coef:
                    if obj.active is False:
                        if obj.focus_non_active_ready:
                            obj.focus_non_active_ready = False
                            obj.color = obj.color_non_active_focused
                    if obj.active is True:
                        if obj.focus_active_ready:
                            obj.focus_active_ready = False
                            obj.color = obj.color_active_focused

                # Feature - focus light of active / inactive circle - p.2
                if distance > obj.radius * self.drawing_coef:
                    if obj.active is False:
                        obj.color = obj.color_non_active_non_focused
                        obj.focus_non_active_ready = True
                    if obj.active is True:
                        obj.color = obj.color_active_non_focused
                        obj.focus_active_ready = True

                # snapping Interactive Circle to mouse cursor while active = True
                if obj.movable and obj.active:
                    obj.color = obj.color_active_focused
                    obj.center_point.coordinate_x = mouse_pos[0]
                    obj.center_point.coordinate_y = mouse_pos[1]

                # change status of Interactive circle by mouse click
                if mouse_up:
                    if distance < obj.radius * self.drawing_coef:
                        if obj.active:
                            obj.active = False
                        else:
                            obj.active = True
            elif isinstance(obj, MovableCircle):
                obj: MovableCircle

                # apply sectoring
                obj.sector_x = obj.vector.dot.coordinate_x // self.segment_dimension_x
                obj.sector_y = obj.vector.dot.coordinate_y // self.segment_dimension_y

                # CONDITION - WALL HIT
                if obj.center_point.coordinate_y < self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.center_point.coordinate_y = self.boundary_for_moving_objects
                    obj.vector.degree = self.mirror_angle_by_x_axis(obj.vector.degree)
                elif obj.center_point.coordinate_y > self.field_coordinate_y - self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.center_point.coordinate_y = self.field_coordinate_y - self.boundary_for_moving_objects
                    obj.vector.degree = self.mirror_angle_by_x_axis(obj.vector.degree)
                elif obj.center_point.coordinate_x < self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.center_point.coordinate_x = self.boundary_for_moving_objects + 1
                    obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)
                elif obj.center_point.coordinate_x > self.field_coordinate_x - self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.center_point.coordinate_x = self.field_coordinate_x - self.boundary_for_moving_objects - 1
                    obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)

                # GENERAL - LINEAR MOVEMENT BY VECTOR
                if obj.vector.energy > 0:
                    obj.vector.dot.coordinate_x += math.floor(
                        (dt * (obj.vector.energy / 100)) * math.cos(math.radians(obj.vector.degree)))
                    obj.vector.dot.coordinate_y += math.floor(
                        (dt * (obj.vector.energy / 100)) * math.sin(math.radians(obj.vector.degree)))
                    # obj.vector.energy -= 1

                obj.vector.energy = round(obj.vector.energy, 3)
            elif isinstance(obj, ChainPiece):
                obj: ChainPiece

                if obj.next_link is not None:

                    distance = math.floor(
                        math.sqrt((obj.center_point.coordinate_x - obj.next_link.center_point.coordinate_x) ** 2 + (
                                obj.center_point.coordinate_y - obj.next_link.center_point.coordinate_y) ** 2))

                    raw_angle = round(self.negative_to_positive(math.degrees(
                        math.atan2(obj.next_link.center_point.coordinate_y - obj.center_point.coordinate_y,
                                   obj.next_link.center_point.coordinate_x - obj.center_point.coordinate_x))), 3)

                    dx = math.floor((distance / 5) * math.cos(math.radians(raw_angle)))
                    dy = math.floor((distance / 5) * math.sin(math.radians(raw_angle)))

                    if distance > 1:
                        obj.center_point.coordinate_x += dx
                        obj.center_point.coordinate_y += dy

    def get_set_of_objects(self):
        """
        Set of objects will be returned
        :return:Set of objects
        """
        return self.set_of_objects

    def add_object(self, input_object):
        self.set_of_objects.add(input_object)

    def remove_object(self, input_object):
        self.set_of_objects.remove(input_object)

    @staticmethod
    def mirror_angle_by_y_axis(a):

        answer = a

        if a < 0:
            return a * -1

        if a > 360:
            return a - 360

        if a == 0:
            answer = 180
        elif a == 90:
            answer = 270
        elif a == 180:
            answer = 0
        elif a == 270:
            answer = 180
        elif a == 360:
            answer = 180

        # I - II
        if 0 < a < 90:
            answer = 180 - a
        # II - I
        elif 90 < a < 180:
            answer = a - 2 * (a - 90)

        # III - IV
        if 180 < a < 270:
            answer = 540 - a
        elif 270 < a < 360:
            answer = 540 - a
        # return answer + random.randint(0, 15)
        return answer + 1

    @staticmethod
    def mirror_angle_by_x_axis(a):

        answer = a

        if a < 0:
            return a * -1

        if a > 360:
            return a - 360

        if a == 0:
            answer = 180
        elif a == 90:
            answer = 270
        elif a == 180:
            answer = 0
        elif a == 270:
            answer = 180
        elif a == 360:
            answer = 180

        # I - IV
        if 0 < a < 90:
            answer = 360 - a
        # IV - I
        elif 270 < a < 360:
            answer = 360 - a

        # II - III
        if 90 < a < 180:
            answer = 360 - a
        # III - II
        elif 180 < a < 270:
            answer = 360 - a

        # return answer + random.randint(0, 15)
        return answer + 1

    @staticmethod
    def negative_to_positive(a):
        angle = a % 360
        if angle < 0:
            angle += 360
        return angle
