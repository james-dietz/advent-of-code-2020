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

    def check(self, input_int: int) -> bool:
        """
        Test the provided integer and return whether it sits within the declared range.
        The specified range is inclusive at both ends.
        :param input_int: the integer to test
        :return: whether the integer is within the range
        """
        return self.min <= input_int <= self.max


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
    def __init__(self, rules: List[Union[RegexRule, RangeRule, LengthRule]]):
        self.rules = rules

    def check(self, input: Any) -> bool:
        """
        Test the input against all of the rules provided.
        :param input: the input under test
        :return: true if all rule checks return true, else false
        """
        pass
