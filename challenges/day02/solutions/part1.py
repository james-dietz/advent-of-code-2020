from typing import Tuple


def parse_policy(line: str) -> Tuple[str, int, int]:
    """
    Parse a password policy, returning the required letter, and the minimum and maximum number of times it must occur.
    :param line: the line to parse
    :return: a tuple containing the password policy
    """
    policy, _ = line.split(sep=": ")
    character = policy[-1]
    min_occurrences, max_occurrences = policy.split(" ")[0].split("-")
    return character, int(min_occurrences), int(max_occurrences)
