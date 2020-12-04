import unittest

from challenges.day04.solutions.part2 import LengthRule, RangeRule, RegexRule, SetMemberRule, And, Or


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


class TestRegexRule(unittest.TestCase):
    def setUp(self) -> None:
        self.regex_rule = RegexRule(pattern=r"\d+(cm|in)")

    def test_regex_match(self):
        self.assertTrue(self.regex_rule.check("160cm"))
        self.assertTrue(self.regex_rule.check("40in"))
        self.assertFalse(self.regex_rule.check("jiffy"))


class TestSetMemberRule(unittest.TestCase):
    def setUp(self) -> None:
        self.set_rule = SetMemberRule(set={"byr", "eyr", "iyr"})

    def test_set_member_match(self):
        self.assertTrue(self.set_rule.check("byr"))
        self.assertFalse(self.set_rule.check("$$$"))


class TestAndRule(unittest.TestCase):
    def setUp(self) -> None:
        self.regex_rule = RegexRule(r"\d{4}")
        self.length_rule = LengthRule(exact=4)
        self.and_rule = And(rules=[self.regex_rule, self.length_rule])

    def test_and_match(self):
        # both rules pass
        self.assertTrue(self.and_rule.check("4321"))
        # length rule fails
        self.assertFalse(self.and_rule.check("54321"))
        # regex rule fails
        self.assertFalse(self.and_rule.check("abcd"))


class TestOrRule(unittest.TestCase):
    def setUp(self):
        self.regex_rule = RegexRule(r"[0-9a-f]{2,}")
        self.length_rule = LengthRule(exact=4)
        self.or_rule = Or(rules=[self.regex_rule, self.length_rule])

    def test_or_match(self):
        # matches neither rule
        self.assertFalse(self.or_rule.check("clips"))
        # matches regex
        self.assertTrue(self.or_rule.check("789abcdef"))
        # matches length
        self.assertTrue(self.or_rule.check("1234"))
        # matches both
        self.assertTrue(self.or_rule.check("beef"))


if __name__ == '__main__':
    unittest.main()
