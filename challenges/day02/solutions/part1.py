from typing import Tuple

Policy = Tuple[str, int, int]


def parse_policy(line: str) -> Tuple[Policy, str]:
    """
    Parse a password policy, returning the required letter, and the minimum and maximum number of times it must occur.
    :param line: the line to parse
    :return: a tuple containing the password policy, and the password
    """
    policy, password = line.split(sep=": ")
    character = policy[-1]
    min_occurrences, max_occurrences = policy.split(" ")[0].split("-")
    return (character, int(min_occurrences), int(max_occurrences)), password


def is_valid_password(policy: Policy, password: str) -> bool:
    """
    Tests whether the provided password conforms to the password policy.
    :param policy: The character required to be present and the range of possible occurrences
    :param password: The password to test
    :return: Whether the password is valid or not
    """
    pass
