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
