import unittest

from challenges.day01.solutions.part1 import subset_sum


class TestSubsetSum(unittest.TestCase):
    """
    Unit tests for the subset sum algorithm, used in the solution for day 1 part 1.
    """
    def setUp(self) -> None:
        self.input = [25, 60, 73, 81]

    def test_subset_sum_success(self):
        target = 133
        self.assertEqual(subset_sum(self.input, target), [60, 73])

    def test_subset_sum_failure(self):
        target = 120
        self.assertEqual(subset_sum(self.input, target), [])


if __name__ == '__main__':
    unittest.main()
