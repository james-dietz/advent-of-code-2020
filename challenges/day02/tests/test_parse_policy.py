import unittest

from challenges.day02.solutions.part1 import parse_policy, is_valid_password


class TestParsePasswordPolicy(unittest.TestCase):
    inputs = [
        ("1-3 a: abcde", ("a", 1, 3), "abcde", True),
        ("1-3 b: cdefg", ("b", 1, 3), "cdefg", False),
        ("2-9 c: ccccccccc", ("c", 2, 9), "ccccccccc", True)
    ]

    def test_parse(self):
        for line, expected_policy, password, _ in self.inputs:
            self.assertEqual(parse_policy(line), (expected_policy, password))

    def test_is_valid_password(self):
        for line, policy, password, is_valid in self.inputs:
            self.assertEqual(is_valid_password(policy, password), is_valid)


if __name__ == '__main__':
    unittest.main()
