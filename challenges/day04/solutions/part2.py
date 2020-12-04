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
        :param input_int: the integer to test
        :return: whether the integer is within the range
        """
        pass