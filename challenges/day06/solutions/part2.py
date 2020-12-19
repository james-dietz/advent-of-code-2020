from typing import Tuple, Set

from challenges.day06.solutions.part1 import split_into_groups


def group_questions_all_answered(person_answered: Tuple[str]) -> Set[str]:
    """
    Find the set of questions for which all passengers answered yes.
    :param person_answered: The questions each person in the group answered yes to.
    :return: The set of questions for which all passengers answered yes
    """
    if len(person_answered) == 1:
        return set(question for question in person_answered[0])
    else:
        questions_answered = set(question for question in person_answered[0])
        for questions in person_answered[1:]:
            question_set = set(question for question in questions)
            questions_answered.intersection_update(question_set)

    return questions_answered


def solve_part2(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        groups = split_into_groups([line.rstrip("\n") for line in input_file.readlines()])
        total = 0
        for group in groups:
            total += len(group_questions_all_answered(group))
        return total


if __name__ == '__main__':
    print(solve_part2("../inputs/input.txt"))