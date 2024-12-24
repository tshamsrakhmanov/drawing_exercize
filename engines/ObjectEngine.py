import math
from objects.InteractiveObjects import PinBoardCircle, GradientCircle, MovableCircle, Vector, Line, ChainPiece
from objects.GeometryObjects import Geometry, Dot
from settings.colors import *


class ObjectsEngine:
    # to resolve out-of bounds movement

    def __init__(self, WIDTH: int, HEIGHT: int, coef: int, segments: int):
        """
        Init of objects engine
         - create empty set of objects
         - t.b.d. later with additional info
        """
        self.set_of_objects = set()
        self.ticker_cache = None
        self.field_coordinate_x = WIDTH * coef
        self.field_coordinate_y = HEIGHT * coef
        self.drawing_coef = coef
        self.energy_loss = 0.85
        self.boundary_for_moving_objects = 500
        self.sectoring_factor = segments
        self.segment_dimension_x = int(self.field_coordinate_x / self.sectoring_factor)
        self.segment_dimension_y = int(self.field_coordinate_x / self.sectoring_factor)
        self.timer = 0
        self.time_previous = 0
        self.started = False

    # def get_field(self):
    #     return self.field_coordinate_x, self.field_coordinate_y

    def get_objects_by_adjacent_sector(self, sector_id_x_input: int, sector_id_y_input, obj_self):

        answer = set(filter(lambda x: isinstance(x, MovableCircle) and
                                      x.sector_x - 1 <= sector_id_x_input <= x.sector_x + 1 and
                                      x.sector_y - 1 <= sector_id_y_input <= x.sector_y + 1 and
                                      x != obj_self, self.set_of_objects))

        return answer

    def update_set_of_objects(self, mouse_pos: tuple, mouse_up: bool, mouse_down: bool, kb_space: bool, demo_name: str,
                              dt: int):
        """
        By evoking this method ObjectEngine will update status and all relevant parameters of all objects in modeling space
        :param mouse_pos: provide coordinates of mouse position on the screen
        :param mouse_up: detection of mouse release button
        :param mouse_down: detection of mouse press button
        :return: None
        """

        # Reset scene by space keyboard invoke - avaliable each 1000 secs
        # self.timer += dt

        # if self.timer > self.time_previous + 1000 and self.started:
        #     self.set_of_objects.clear()
        #     self.started = False
        #     self.time_previous = 0
        #     self.timer = 0

        if kb_space and not self.started:
            self.started = True
            if demo_name == 'sample_collisions':
                self.set_of_objects.clear()
                for i in range(72):
                    temp_dot = Dot((mouse_pos[0]) + random.randint(-1000, 1000),
                                   (mouse_pos[1]) + random.randint(-1000, 1000))
                    vector_1 = Vector(float(i * 5.5), temp_dot, energy_input=float(random.randint(100, 2000)))
                    movable_circle = MovableCircle(vector_1, i_dot=temp_dot, i_radius=random.randint(5, 25),
                                                   i_color=COLOR_RANDOM())
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
                dot_tail = Dot(self.field_coordinate_x * 3 / 4, self.field_coordinate_y / 4)
                dot_head = Dot(self.field_coordinate_x * 3 / 4, self.field_coordinate_y / 2)
                i_line1 = Line(dot_tail, dot_head, COLOR_RED, False, COLOR_RED, COLOR_RED)
                sneak_head = ChainPiece(None, link_size=500, i_dot=dot_head, i_radius=30, i_color=COLOR_TEAL)
                sneak_tail = ChainPiece(sneak_head, link_size=500, i_dot=dot_tail, i_radius=30, i_color=COLOR_TEAL)
                self.add_object(sneak_tail)
                self.add_object(sneak_head)
                self.add_object(i_line1)

        """
        # TODO this piece of code generates solution for demo iterativly by time slice.
        #  Need to rework as option flag to program execution - if demo will be resterted.
        # self.timer += dt
        #
        # if self.timer > self.time_previous + 5000:
        #     self.set_of_objects.clear()
        #     self.time_previous = 0
        #     self.timer = 0
        #
        #     temp_x = random.randint(500, self.field_coordinate_x)
        #     temp_y = random.randint(500, self.field_coordinate_y)
        #     for i in range(72):
        #         temp_dot = Dot(temp_x + random.randint(-1000, 1000), temp_y + random.randint(-1000, 1000))
        #         vector_1 = Vector(float(i * 5.5), temp_dot, energy_input=float(random.randint(100, 2000)))
        #         movable_circle = MovableCircle(vector_1, i_dot=temp_dot, i_radius=random.randint(5, 25),
        #                                        i_color=COLOR_RANDOM())
        #         self.add_object(movable_circle)

        # TODO turn on  this feature only when it'll be needed to optimize FPS for large quantities of objects with collisions
        # Separate algorythm to apply sector id to objects:
        # for obj in self.set_of_objects:
        #     if isinstance(obj, MovableCircle):
        #         obj.sector_x = obj.vector.dot.x // self.segment_dimension_x
        #         obj.sector_y = obj.vector.dot.y // self.segment_dimension_y
        """

        for obj in self.set_of_objects:
            if isinstance(obj, GradientCircle):

                """
                GRADIENT CIRCLE FACILITATION
                Sort-of-implementation due to enormous volume of fine tuning
                This values of proportions are tested /good/ with following matrix:

                '
                distance = 40

                for i in range(1, 38): # 38
                    for y in range(1, 19): # 19
                        temp_dot = Dot(distance * i, distance * y)
                        objects_buffer.append(
                            GradientCircle(i_dot=temp_dot, i_radius=10, i_color=COLOR_WHITE))
                '
                """

                distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

                max_dist = 40 * self.drawing_coef
                min_dist = 1
                delta_dist = max_dist - min_dist

                if distance >= obj.radius * max_dist:
                    obj.actual_size = obj.radius * 2
                    obj.color = COLOR_GREEN
                elif obj.radius * min_dist <= distance < obj.radius * max_dist:
                    coeff_1 = (distance - min_dist * obj.radius) / (delta_dist * obj.radius)
                    obj.actual_size = int(
                        (obj.radius / 2) + (1.5 * obj.radius) * coeff_1)
                    obj.color = (int(255 - 255 * coeff_1), int(0 + 255 * coeff_1), 0)
                else:
                    obj.actual_size = int(obj.radius / 4)
                    obj.color = COLOR_RED
            elif isinstance(obj, PinBoardCircle):

                # TODO implement distance calculation only for PinBoardCircle's only reachable for mouse in certain sector (with feature implemented, ofc)
                distance = math.sqrt((mouse_pos[0] - obj.dot_start.x) ** 2 + (mouse_pos[1] - obj.dot_start.y) ** 2)

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
                    obj.dot_start.x = mouse_pos[0]
                    obj.dot_start.y = mouse_pos[1]

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
                obj.sector_x = obj.vector.dot.x // self.segment_dimension_x
                obj.sector_y = obj.vector.dot.y // self.segment_dimension_y

                # CONDITION - WALL HIT
                if obj.dot_start.y < self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.dot_start.y = self.boundary_for_moving_objects
                    obj.vector.degree = self.mirror_angle_by_x_axis(obj.vector.degree)
                elif obj.dot_start.y > self.field_coordinate_y - self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.dot_start.y = self.field_coordinate_y - self.boundary_for_moving_objects
                    obj.vector.degree = self.mirror_angle_by_x_axis(obj.vector.degree)
                elif obj.dot_start.x < self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.dot_start.x = self.boundary_for_moving_objects + 1
                    obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)
                elif obj.dot_start.x > self.field_coordinate_x - self.boundary_for_moving_objects:
                    obj.vector.energy *= self.energy_loss
                    obj.dot_start.x = self.field_coordinate_x - self.boundary_for_moving_objects - 1
                    obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)

                # CONDITION - ANOTHER BALL HIT
                # for adjacent_obj in self.get_objects_by_adjacent_sector(obj.sector_x, obj.sector_y, obj):
                #
                #     distance = math.sqrt(
                #         (obj.dot_start.x - adjacent_obj.dot_start.x) ** 2 + (
                #                 obj.dot_start.y - adjacent_obj.dot_start.y) ** 2)
                #
                #     if distance < obj.radius * 35:
                #         print('HIT')
                #         obj.vector.degree, adjacent_obj.vector.degree = adjacent_obj.vector.degree, obj.vector.degree
                #         obj.vector.energy *= self.energy_loss
                #     else:
                #         pass
                # obj.vector.degree = self.mirror_angle_by_y_axis(obj.vector.degree)
                # adjacent_obj.vector = self.mirror_angle_by_x_axis(adjacent_obj.vector.degree)

                # GENERAL - LINEAR MOVEMENT BY VECTOR
                if obj.vector.energy > 0:
                    obj.vector.dot.x += math.floor(
                        (dt * (obj.vector.energy / 100)) * math.cos(math.radians(obj.vector.degree)))
                    obj.vector.dot.y += math.floor(
                        (dt * (obj.vector.energy / 100)) * math.sin(math.radians(obj.vector.degree)))
                    obj.vector.energy -= 1

                obj.vector.energy = round(obj.vector.energy, 3)

            elif isinstance(obj, ChainPiece):
                obj: ChainPiece
                obj.next_link: ChainPiece

                # temp - forced moving of head (non-empty-prev-chain piece)
                if obj.next_link is None:
                    obj.dot_start.x -= 10
                    obj.dot_start.y -= 5
                else:
                    distance = math.floor(math.sqrt((obj.dot_start.x - obj.next_link.dot_start.x) ** 2 + (
                            obj.dot_start.y - obj.next_link.dot_start.y) ** 2))

                    segmentation = (distance / 200)

                    if distance < 1500:
                        print(math.floor(distance))
                    else:
                        if obj.dot_start.x < obj.next_link.dot_start.x and obj.dot_start.y < obj.next_link.dot_start.y:
                            obj.dot_start.x += math.floor(segmentation * math.cos(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x)))
                            obj.dot_start.y += math.floor(segmentation * math.sin(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x)))
                        elif obj.dot_start.x < obj.next_link.dot_start.x and obj.dot_start.y > obj.next_link.dot_start.y:
                            obj.dot_start.x += math.floor(segmentation * math.cos(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x)))
                            obj.dot_start.y -= math.floor(segmentation * math.sin(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x)))
                        elif obj.dot_start.x > obj.next_link.dot_start.x and obj.dot_start.y < obj.next_link.dot_start.y:
                            obj.dot_start.x -= math.floor(segmentation * math.cos(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x)))
                            obj.dot_start.y += math.floor(segmentation * math.sin(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x)))
                        elif obj.dot_start.x > obj.next_link.dot_start.x and obj.dot_start.y > obj.next_link.dot_start.y:
                            obj.dot_start.x -= segmentation * math.cos(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x))
                            obj.dot_start.y -= segmentation * math.sin(
                                math.atan2(obj.next_link.dot_start.y, obj.next_link.dot_start.x))


    def get_set_of_objects(self):
        """
        Set of objects will be returned
        :return:Set of objects
        """
        return self.set_of_objects

    def add_object(self, input_object: Geometry):
        self.set_of_objects.add(input_object)

    def remove_object(self, input_object: Geometry):
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
