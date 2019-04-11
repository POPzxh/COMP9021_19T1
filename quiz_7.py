# Randomly fills a grid with True and False, with width, height and density
# controlled by user input, and computes the number of all "good paths" that link
# a point of coordinates (x1, y1) to a point of coordinates (x2, y2)
# (x1 and x2 are horizontal coordinates, increasing from left to right,
# y1 and y2 are vertical coordinates, increasing from top to bottom,
# both starting from 0), that is:
# - paths that go through nothing but True values in the grid
# - paths that never go through a given point in the grid more than once;
# - paths that never keep the same direction (North, South, East, West) over
#   a distance greater than 2.
#
# Written by *** and Eric Martin for COMP9021

from collections import namedtuple
import numpy as np
from random import seed, randrange
import sys

Point = namedtuple('Point', 'x y')


def display_grid():
    for row in grid:
        print('   ', ' '.join(str(int(e)) for e in row))


def valid(pt):
    return 0 <= pt.x < width and 0 <= pt.y < height


operation = {
    'N': lambda pt: Point(pt.x, pt.y-1),
    'S': lambda pt: Point(pt.x, pt.y+1),
    'W': lambda pt: Point(pt.x-1, pt.y),
    'E': lambda pt: Point(pt.x+1, pt.y),
}


# 没办法了，只能改函数签名了
def nb_of_good_paths(pt_1, pt_2, state):
    if get_value_of_point(pt_1) == 0:
        return 0
    if pt_1 == pt_2:
        return 1
    grid[pt_1.y][pt_1.x] = 0
    # number = sum(
    #     # ↓↓↓我是故意的↓↓↓ 想抄代码先听课
    #     nb_of_good_paths(op[1](pt_1), pt_2, (op[0], 1 if state[0] != op[0] else state[1]+1))
    #     for op in operation.items() if state[0] != op[0] or state[1] < 2
    # )
    number = 0
    for op in operation.items():
        if state[0] != op[0]:
            number += nb_of_good_paths(op[1](pt_1), pt_2, (op[0], 1))
        elif state[1] < 2:
            number += nb_of_good_paths(op[1](pt_1), pt_2, (op[0], state[1]+1))
    grid[pt_1.y][pt_1.x] = 1
    return number


def get_value_of_point(pt):
    if not valid(pt):
        return 0
    return grid[pt.y][pt.x]


try:
    for_seed, density, height, width = (abs(int(i)) for i in
                                        input('Enter four integers: ').split()
                                        )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not density:
    density = 1
seed(for_seed)
grid = np.array([randrange(density) > 0
                 for _ in range(height * width)
                 ]
                ).reshape((height, width))
print('Here is the grid that has been generated:')
display_grid()
try:
    i1, j1, i2, j2 = (int(i) for i in input('Enter four integers: ').split())
    pt_1 = Point(i1, j1)
    pt_2 = Point(i2, j2)
    if not valid(pt_1) or not valid(pt_2):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('Will compute the number of good paths '
      f'from ({pt_1.x}, {pt_1.y}) to ({pt_2.x}, {pt_2.y})...'
      )

paths_nb = nb_of_good_paths(pt_1, pt_2, (None, None))

if not paths_nb:
    print('There is no good path.')
elif paths_nb == 1:
    print('There is a unique good path.')
else:
    print('There are', paths_nb, 'good paths.')
