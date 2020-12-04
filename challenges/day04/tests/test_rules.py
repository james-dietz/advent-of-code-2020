import unittest

from challenges.day04.solutions.part2 import LengthRule, RangeRule, RegexRule, SetMemberRule, And, Or, \
    is_passport_valid, extract_passport_fields


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


class TestPassportVerification(unittest.TestCase):
    inputs = [
        ("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f", True),
        ("eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm", True),
        ("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022", True),
        ("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719", True),
        ("eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926", False),
        ("iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946", False),
        ("hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277", False),
        ("hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007", False)
    ]

    def test_passport_verification(self):
        for passport, is_valid in self.inputs:
            self.assertEqual(is_passport_valid(passport), is_valid)

    def test_field_extraction(self):
        input = "pid:087499704 hgt:74in ecl:grn"
        expected = {"pid": "087499704", "hgt": "74in", "ecl":"grn"}
        self.assertEqual(extract_passport_fields(input), expected)


if __name__ == '__main__':
    unittest.main()
