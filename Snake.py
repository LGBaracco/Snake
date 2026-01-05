""" Class: Snake
Created on 02 dic. 2020
@author: L.G.Baracco """

from Coordinate import Coordinate


class Snake:

    DEFAULT_REMOVE_INDEX = -1

    def __init__(self, starting_point, starting_point1, direction, width_limit, height_limit):
        self.coordinates = [starting_point, starting_point1]
        self.direction = direction
        self.WIDTH_LIMIT = width_limit
        self.HEIGHT_LIMIT = height_limit

    def add_head(self, ui):
        element = Coordinate(self.coordinates[0].x, self.coordinates[0].y)
        element.shift(self.direction)

        self.coordinates.insert(0, element)
        self.move_through_wall(0)

        ui.place(self.coordinates[0].x, self.coordinates[0].y, ui.SNAKE)

        return element

    def add_tail(self, ui):
        element = Coordinate(self.coordinates[-1].x, self.coordinates[-1].y)

        help_x = self.coordinates[-2].x - element.x
        help_y = self.coordinates[-2].y - element.y

        element.shift_values(-help_x, -help_y)

        self.coordinates.append(element)
        self.move_through_wall(-1)
        ui.place(self.coordinates[-1].x, self.coordinates[-1].y, ui.SNAKE)

        return element

    def remove(self, ui, index=DEFAULT_REMOVE_INDEX):

        ui.place(self.coordinates[index].x, self.coordinates[index].y, ui.EMPTY)
        return self.coordinates.pop(index)

    def move(self, ui):

        self.remove(ui)
        self.add_head(ui)

    def move_through_wall(self, index):
        if self.coordinates[index].x < 0:
            self.coordinates[index].x = self.WIDTH_LIMIT

        elif self.coordinates[index].x > self.WIDTH_LIMIT:
            self.coordinates[index].x = 0

        elif self.coordinates[index].y < 0:
            self.coordinates[index].y = self.HEIGHT_LIMIT

        elif self.coordinates[index].y > self.HEIGHT_LIMIT:
            self.coordinates[index].y = 0

    def set_direction(self, direction):
        if direction != self.direction:
            if (direction != 'r' or self.direction != 'l') and (direction != 'l' or self.direction != 'r') and \
                    (direction != 'u' or self.direction != 'd') and (direction != 'd' or self.direction != 'u'):
                self.direction = direction

    def dead(self, walls=None):
        for i in range(1, len(self.coordinates)):
            if self.coordinates[0] == self.coordinates[i] or self.coordinates[-1] == self.coordinates[i-1]:
                return True

        if walls is not None:
            for wall in walls:
                if self.coordinates[0] == wall or self.coordinates[-1] == wall:
                    return True

        return False

    def won(self, max_length):
        if len(self.coordinates) == max_length:
            return True
        else:
            return False
