import unittest

from challenges.day02.solutions.part1 import parse_policy


class TestParsePasswordPolicy(unittest.TestCase):
    inputs = [
        ("1-3 a: abcde", ("a", 1, 3)),
        ("1-3 b: cdefg", ("b", 1, 3)),
        ("2-9 c: ccccccccc", ("c", 2, 9))
    ]

    def test_parse(self):
        for line, expected_policy in self.inputs:
            self.assertEqual(parse_policy(line), expected_policy)


if __name__ == '__main__':
    unittest.main()
