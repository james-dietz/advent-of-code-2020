from typing import Set, List

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
OPTIONAL_FIELDS = {"cid"}


def extract_passport_fields(passport: str) -> Set[str]:
    """
    Extract the passport fields from a given passport string.
    :param passport: The passport being processed
    :return: A set containing all of the extracted fields.
    """
    return set(item.split(":")[0] for item in passport.split(" "))


def is_passport_valid(fields: Set[str]) -> bool:
    """
    Check if a passport is valid, under the following criteria:
        - all fields specified by REQUIRED_FIELDS must be present for a passport to be valid
        - fields specified by OPTIONAL_FIELDS may or may not be present
    :param fields: a set containing the fields found in the passport
    :return: whether the passport meets the above criteria
    """
    return REQUIRED_FIELDS.issubset(fields)


def sanitise_chunk(input: List[str]) -> str:
    """
    Merge separate passport lines into one single line.
    :param input: a series of lines
    :return: the lines, combined and space-separated
    """
    return " ".join(input)


def separate_passports(input_lines: List[str]) -> List[List[str]]:
    """
    Split up passports from the input file. Blank lines delimit each passport.
    :param input_lines: A list of lines from the input file
    :return: A list of lists of passport lines to be combined and processed.
    """
    passports = []
    current_passport_lines = []
    for line in input_lines:
        if line == "":
            passports.append(current_passport_lines)
            current_passport_lines = []
        else:
            current_passport_lines.append(line)
    return passports


def solve_part1(input_filename: str) -> int:
    valid_passports = 0
    with open(input_filename, "r") as input_file:
        # read the file
        lines = [line.strip("\n") for line in input_file.readlines()]
        # split the file into passports
        passport_lines = separate_passports(lines)
        for passport_line_list in passport_lines:
            # combine lines into one passport
            passport = sanitise_chunk(passport_line_list)
            # get the passport fields
            fields = extract_passport_fields(passport)
            # count passport if valid
            valid_passports += is_passport_valid(fields)
    return valid_passports


if __name__ == '__main__':
    print(solve_part1("../inputs/input.txt"))