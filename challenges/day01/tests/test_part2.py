import unittest

from challenges.day01.solutions.part2 import three_sum


class Test3SUM(unittest.TestCase):
    """
    Unit tests for the 3SUM algorithm, used to solve part 2 of day 1's challenge.
    """
    def setUp(self) -> None:
        self.input = [5, 11, 17, 23, 29]

    def test_three_sum_success(self):
        target = 45
        self.assertEqual(three_sum(self.input, target), [5, 17, 23])

    def test_three_sum_failure(self):
        target = 67
        self.assertEqual(three_sum(self.input, target), [])


if __name__ == '__main__':
    unittest.main()
