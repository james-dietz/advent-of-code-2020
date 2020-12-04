from typing import Tuple

TREE = "#"
BLANK = "."
KNIGHT_MOVEMENT = (3, 1)  # three cells right, one cell down


def trees_encountered(input: str, move: Tuple[int, int]) -> int:
    """
    Count the number of trees encountered while walking the path specified by the size of each movement step.
    The input is a string representation of a forest with origin top left (0, 0), +x rightward, +y downward.
    :param input: the forest to path through
    :param move:  the movement in cells [horizontal, vertical] for each step
    :return: The number of trees encountered.
    """
    forest = [[cell for cell in line] for line in input.split("\n")]
    # specify a cell (x, y) in the forest using forest[y][x]
    max_x, max_y = len(forest[0]), len(forest) - 1
    x, y = (0, 0)
    trees = 0
    # walk until we reach the bottom row
    while y < max_y - 1:
        # forest wraps around in the x-axis
        x = (x + move[0]) % max_x
        y += move[1]
        # count a tree if there is one in the cell (True == 1; False == 0)
        trees += forest[y][x] == TREE
    return trees


def solve_part1(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        forest = input_file.read()
        return trees_encountered(forest, KNIGHT_MOVEMENT)


if __name__ == '__main__':
    print(solve_part1("../inputs/input.txt"))
