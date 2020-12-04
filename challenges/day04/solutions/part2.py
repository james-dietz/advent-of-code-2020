import re
from typing import Set, List, Any, Union


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
    "hcl": SetMemberRule({"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}),
    "pid": RegexRule(r"[0-9]{9}")
}


def is_passport_valid(passport: str) -> bool:
    """
    Tests whether the passport is valid according to the predefined rules.
    :param passport: The passport to test
    :return: True if the passport is valid, else false
    """
    pass