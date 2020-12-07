import re
import string
from typing import Set, List, Any, Union, Dict

from challenges.day04.solutions.part1 import separate_passports, sanitise_chunk


class LengthRule:
    def __init__(self, exact=4):
        self.exact_length = exact

    def check(self, input_str: str) -> bool:
        """
        Check if the provided string meets the criteria set when the rule was initialised.
        :param input_str: The string to test
        :return: whether the string meets the criteria
        """
        return len(input_str) == self.exact_length


class RangeRule:
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def check(self, input: Union[str, int]) -> bool:
        """
        Test the provided integer and return whether it sits within the declared range.
        The specified range is inclusive at both ends.
        :param input: the integer to test
        :return: whether the integer is within the range
        """
        if isinstance(input, str):
            input = input.translate(
                str.maketrans("", "", string.ascii_letters)
            )
            return input.isnumeric() and (self.min <= int(input) <= self.max)
        return self.min <= input <= self.max


class RegexRule:
    def __init__(self, pattern: str):
        self.pattern = re.compile(pattern)

    def check(self, input_str: str) -> bool:
        """
        Test the provided string against the set regex expression.
        :param input_str: the string to test
        :return: whether the pattern matches the provided string
        """
        return re.match(self.pattern, input_str) is not None


class SetMemberRule:
    def __init__(self, set: Set[str]):
        self.set = set

    def check(self, input_str: str) -> bool:
        """
        Check whether the provided input string is a member of the set
        :param input_str: the string to test
        :return: whether the string is a member of the set
        """
        return input_str in self.set


class And:
    def __init__(self, rules: List[Union[RegexRule, RangeRule, LengthRule, SetMemberRule]]):
        self.rules = rules

    def check(self, input: Any) -> bool:
        """
        Test the input against all of the rules provided.
        :param input: the input under test
        :return: true if all rule checks return true, else false
        """
        return all([rule.check(input) for rule in self.rules])


class Or:
    def __init__(self, rules: List[Union[RangeRule, RegexRule, LengthRule, SetMemberRule, And]]):
        self.rules = rules

    def check(self, input: Any) -> bool:
        """
        Checks whether the input matches any of the provided rules.
        :param input: the input under test
        :return: true if the input matches any of the rules, otherwise false
        """
        return any([rule.check(input) for rule in self.rules])


FOUR_DIGIT_RULE = RegexRule(r"[0-9]{4}")

PASSPORT_RULES = {
    "byr": And([FOUR_DIGIT_RULE, RangeRule(min=1920, max=2002)]),
    "iyr": And([FOUR_DIGIT_RULE, RangeRule(min=2010, max=2020)]),
    "eyr": And([FOUR_DIGIT_RULE, RangeRule(min=2020, max=2030)]),
    "hgt": Or([
        And([RegexRule(r"\d+cm"), RangeRule(min=150, max=193)]),
        And([RegexRule(r"\d+in"), RangeRule(min=59, max=76)])
    ]),
    "hcl": RegexRule(r"#[0-9a-f]{6}"),
    "ecl": SetMemberRule({"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}),
    "pid": RegexRule(r"[0-9]{9}$")
}


def is_passport_valid(passport: str) -> bool:
    """
    Tests whether the passport is valid according to the predefined rules.
    :param passport: The passport to test
    :return: True if the passport is valid, else false
    """
    required_fields = set(PASSPORT_RULES.keys())
    fields = extract_passport_fields(passport)
    if not required_fields.issubset(fields):
        return False

    for field, value in fields.items():
        if field in PASSPORT_RULES.keys():
            test = PASSPORT_RULES[field]
            if not test.check(value):
                return False

    return True


def extract_passport_fields(passport: str) -> Dict[str, str]:
    """
    Extract the fields from a given passport string.
    :param passport: The passport being processed
    :return: A dictionary of key-value pairs extracted from the passport
    """
    return {k: v for k, v in [item.split(":") for item in passport.split(" ")]}


def solve_part2(input_filename: str) -> int:
    valid_passports = 0
    with open(input_filename, "r") as input_file:
        # read the file
        lines = [line.strip("\n") for line in input_file.readlines()]
        # split the file into passports
        passport_lines = separate_passports(lines)
        for passport_line_list in passport_lines:
            # combine lines into one passport
            passport = sanitise_chunk(passport_line_list)
            # count passport if valid
            valid = is_passport_valid(passport)
            if valid:
                print(f"{passport:>80} | {valid}")
            valid_passports += valid
    return valid_passports


if __name__ == '__main__':
    print(solve_part2("../inputs/input.txt"))