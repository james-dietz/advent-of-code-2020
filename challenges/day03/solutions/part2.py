from math import prod

from challenges.day03.solutions.part1 import trees_encountered, KNIGHT_MOVEMENT


def solve_part2(input_filename: str):
    movement_types = [(1, 1), KNIGHT_MOVEMENT, (5, 1), (7, 1), (1, 2)]
    with open(input_filename, "r") as input_file:
        forest = input_file.read()
        return prod([trees_encountered(forest, movement) for movement in movement_types])


if __name__ == '__main__':
    print(solve_part2("../inputs/input.txt"))
