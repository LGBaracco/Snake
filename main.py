""" Assignment: snake
Created on 30 nov. 2020
@author: L.G.Baracco """

from libs.ipy_lib import SnakeUserInterface
from Snake import Snake
from Coordinate import Coordinate

WIDTH = 32
HEIGHT = 24
FPS = 10

STARTING_POINT = (1, 0)
STARTING_POINT1 = (0, 0)
DIRECTION = 'r'

walls = []
food = Coordinate(0, 0)


def show_elements(snake, walls=None):
    for block in snake.coordinates:
        ui.place(block.x, block.y, ui.SNAKE)

    if walls is not None:
        for wall in walls:
            ui.place(wall.x, wall.y, ui.WALL)

    ui.show()


def spawn_food():
    global snake
    global walls
    global food

    x = ui.random(WIDTH)
    y = ui.random(HEIGHT)
    food = Coordinate(x, y)

    for coordinate in snake.coordinates:
        if food == coordinate:
            spawn_food()

    if walls is not None:
        for wall in walls:
            if food == wall:
                spawn_food()

    ui.place(food.x, food.y, ui.FOOD)


def eat():
    global snake
    global food

    if snake.coordinates[0] == food:
        snake.add_tail(ui)
        spawn_food()


def event_handler(event):
    if event.name == 'alarm':
        snake.move(ui)
    elif event.name == 'arrow':
        snake.set_direction(event.data)


def level():
    answer = input('Do you want to insert a custom level? (press "yes" if you do, any other key if not): ')
    if answer == 'yes':
        return True

    return False


def load_snake(file):
    coordinates = file[0].splitlines()
    starting_point = coordinates[0].split()
    starting_point1 = coordinates[1].split()

    direction = file[1].lower()

    coordinate = Coordinate(int(starting_point[0]), int(starting_point[1]))
    coordinate1 = Coordinate(int(starting_point1[0]), int(starting_point1[1]))

    return Snake(coordinate, coordinate1, direction, WIDTH-1, HEIGHT-1)


def load_walls(file):
    coordinates = file.splitlines()
    walls = []
    for coordinate in coordinates:
        split_coordinate = coordinate.split()
        wall = Coordinate(int(split_coordinate[0]), int(split_coordinate[1]))
        walls.append(wall)

    return walls


def load_level():
    filename = input('Please type the name or directory of the file: ')

    file = open(filename).read().strip()
    split_file = file.split('=')

    snake = load_snake(split_file[0:2])
    walls = load_walls(split_file[2])

    return snake, walls


if level():
    snake, walls = load_level()
else:
    coordinate = Coordinate(STARTING_POINT[0], STARTING_POINT[1])
    coordinate1 = Coordinate(STARTING_POINT1[0], STARTING_POINT1[1])
    snake = Snake(coordinate, coordinate1, DIRECTION, WIDTH-1, HEIGHT-1)
    walls = None

ui = SnakeUserInterface(WIDTH, HEIGHT)
ui.set_animation_speed(FPS)

spawn_food()

show_elements(snake, walls)

while True:
    event = ui.get_event()
    event_handler(event)

    if snake.dead(walls):
        ui.print_('Game over')
        break
    elif snake.won(WIDTH*HEIGHT):
        ui.print_('Game over, you won!')
        break

    eat()

    ui.show()

ui.stay_open()
