import unittest

from challenges.day04.solutions.part2 import LengthRule


class TestLengthRule(unittest.TestCase):
    def setUp(self) -> None:
        self.length_rule = LengthRule(exact=4)

    def test_length_exact_match(self):
        self.assertTrue(self.length_rule.check("true"))
        self.assertFalse(self.length_rule.check("false"))


if __name__ == '__main__':
    unittest.main()
