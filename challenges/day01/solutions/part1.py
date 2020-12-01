from math import prod
from typing import List


def subset_sum(input: List[int], target: int) -> List[int]:
    """
    Runs the subset sum algorithm on the input list, attempting to find values that sum to the target.
    :param input:  a list of integers
    :param target: the target integer for which a sum should be found

    :returns: a list of integers which sum to the target, or an empty list if no match is found
    """
    # The day 1 part 1 problem states that two integers in the list will sum to the target.
    # We first implement an exhaustive search, iterating through the array using two pointers to check each pair.
    # This algorithm runs in worst-case O(n^2) time.
    max_index = len(input)
    for i in range(max_index):
        j = i + 1
        while j < max_index:
            if input[i] + input[j] == target:
                return [input[i], input[j]]
            else:
                j += 1
    else:
        return []


def solve_part1(input_filename: str) -> int:
    """
    Solve part 1 of day 1's challenge.
    Reads the input file, performs the subset sum operation with target 2020,
    then multiplies the two returned values together to produce the answer.
    :param input_filename: path to the input file
    :return: the solution to the problem.
    """
    with open(input_filename, "r") as input_file:
        input = [int(line.rstrip("\n")) for line in input_file]
        target = 2020
        output = subset_sum(input, target)
        return prod(output)


if __name__ == '__main__':
    print(solve_part1("../inputs/input.txt"))
