import unittest
from typing import List

from challenges.day05 import TestCase
from challenges.day05.solutions.day1 import bsp, seat_id

MAX_ROWS, MAX_COLUMNS = 128, 8


class TestBinarySpacePartitioning(unittest.TestCase):
    # declare test cases:
    # (specifier, (row, column), seat_id)
    test_cases: List[TestCase] = [
        ("FBFBBFFRLR", (44, 5), 357),
        ("BFFFBBFRRR", (70, 7), 567),
        ("FFFBBBFRRR", (14, 7), 119),
        ("BBFFBBFRLL", (102, 4), 820),
    ]

    def test_bsp(self):
        for specifier, seat, _ in self.test_cases:
            self.assertEqual(seat, bsp(specifier, MAX_ROWS, MAX_COLUMNS))

    def test_get_seat_id(self):
        for _, seat, expected_seat_id in self.test_cases:
            self.assertEqual(expected_seat_id, seat_id(seat))


if __name__ == '__main__':
    unittest.main()
