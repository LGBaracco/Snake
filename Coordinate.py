''' Class: Coordinate
Created on 01 dic. 2020
@author: L.G.Baracco '''


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, direction):
        if direction == 'd':
            self.y += 1
        elif direction == 'u':
            self.y -= 1
        elif direction == 'r':
            self.x += 1
        elif direction == 'l':
            self.x -= 1

    def shift_values(self, x=0, y=0):
        self.x += x
        self.y += y

    def __eq__(self, other_object):
        if not isinstance(other_object, Coordinate):
            return False

        return self.x == other_object.x and self.y == other_object.y
