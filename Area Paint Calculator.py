import math


def painting_area(wall_height, wall_width, coverage):
    number_of_cans = 0
    number_of_cans = (wall_height * wall_width) / coverage
    return math.ceil(number_of_cans)


print(painting_area(2, 4, 5))