from challenges.day02.solutions.part1 import Policy, parse_policy


def is_valid_toboggan_password(policy: Policy, password: str) -> bool:
    """
    Test if the password conforms to Toboggan's version of the password policy.
    The policy is interpreted as:
        - the required character must exist in exactly one of the two 1-indexed indices from the policy.
    :param policy: the password policy
    :param password: the password to test
    :return: whether the password is valid or not
    """
    character, i1, i2 = policy
    first = password[i1 - 1] == character
    second = password[i2 - 1] == character
    return first != second


def solve_part2(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        # parse each line's policy and extract the password
        lines = [parse_policy(line.rstrip("\n")) for line in input_file.readlines()]
        # count the number of valid passwords
        return sum([is_valid_toboggan_password(policy, password) for policy, password in lines])


if __name__ == '__main__':
    print(solve_part2("../inputs/input.txt"))
