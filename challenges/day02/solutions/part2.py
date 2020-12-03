from challenges.day02.solutions.part1 import Policy


def is_valid_toboggan_password(policy: Policy, password: str) -> bool:
    """
    Test if the password conforms to Toboggan's version of the password policy.
    The policy is interpreted as:
        - the required character must exist in exactly one of the two 1-indexed indices from the policy.
    :param policy: the password policy
    :param password: the password to test
    :return: whether the password is valid or not
    """
    pass