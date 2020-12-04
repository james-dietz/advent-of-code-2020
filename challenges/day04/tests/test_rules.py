import unittest

from challenges.day04.solutions.part2 import LengthRule, RangeRule


class TestLengthRule(unittest.TestCase):
    def setUp(self) -> None:
        self.length_rule = LengthRule(exact=4)

    def test_length_exact_match(self):
        self.assertTrue(self.length_rule.check("true"))
        self.assertFalse(self.length_rule.check("false"))


class TestRangeRule(unittest.TestCase):
    def setUp(self) -> None:
        self.range_rule = RangeRule(min=1, max=10)

    def test_range_match(self):
        self.assertTrue(self.range_rule.check(5))
        self.assertFalse(self.range_rule.check(13))


if __name__ == '__main__':
    unittest.main()
