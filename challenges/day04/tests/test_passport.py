import unittest
from typing import Tuple, Set, List

from challenges.day04.solutions.part1 import extract_passport_fields, is_passport_valid

InputFormat = Tuple[str, Set[str], bool]


class TestPassportParser(unittest.TestCase):
    inputs: List[InputFormat] = [
        # passport 1: valid, 8 fields present
        (
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
            {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "cid", "hgt"},
            True
        ),
        # passport 2: invalid, height ("hgt") missing
        (
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
            {"iyr", "ecl", "cid", "eyr", "pid", "hcl", "byr"},
            False
        ),
        # passport 3: valid, cid missing but optional
        (
            "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
            {"hcl", "iyr", "eyr", "ecl", "pid", "byr", "hgt"},
            True
        ),
        # passport 4: invalid, byr missing
        (
            "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
            {"hcl", "eyr", "pid", "iyr", "ecl", "hgt"},
            False
        )
    ]

    def test_parse_passport(self):
        for passport, fields, _ in self.inputs:
            self.assertEqual(extract_passport_fields(passport), fields)

    def test_is_passport_valid(self):
        for _, fields, is_valid in self.inputs:
            self.assertEqual(is_passport_valid(fields), is_valid)


if __name__ == '__main__':
    unittest.main()