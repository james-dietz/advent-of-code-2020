import unittest

from challenges.day02.solutions.part1 import parse_policy


class TestParsePasswordPolicy(unittest.TestCase):
    inputs = [
        ("1-3 a: abcde", ("a", 1, 3), "abcde", True),
        ("1-3 b: cdefg", ("b", 1, 3), "cdefg", False),
        ("2-9 c: ccccccccc", ("c", 2, 9), "ccccccccc", True)
    ]

    def test_parse(self):
        for line, expected_policy, password, _ in self.inputs:
            self.assertEqual(parse_policy(line), (expected_policy, password))

if __name__ == '__main__':
    unittest.main()
