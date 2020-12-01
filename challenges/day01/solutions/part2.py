from typing import List


def three_sum(input: List[int], target: int) -> List[List[int]]:
    """
    Implements the 3SUM algorithm (find a subset of order 3 for which the sum is equal to the target value).
    Implementation in O(n^2) worst case time, adapted from https://www.wikiwand.com/en/3SUM#/Quadratic_algorithm.

    :param input: the list of integers to test
    :param target: the target integer
    :return: a list containing the 3 elements whose sum is equal to the target, or an empty list if no match is found
    """
    # Sort the input array (Timsort is O(n log n) worst case).
    input = sorted(input)
    input_length = len(input)
    matches = []
    for i in range(0, input_length - 2):
        a = input[i]
        start, end = i + 1, input_length - 1
        while start < end:
            b, c = input[start], input[end]
            if a + b + c == target:
                matches.append([a, b, c])
                start += 1
                end -= 1
            elif a + b + c > target:
                end -= 1
            else:
                start += 1
    return matches
