from typing import Set, List


def group_questions_answered(questions: List[str]) -> Set[str]:
    """
    Return the set of questions for which at least one person answered correctly.
    :param questions: the questions each person answered correctly
    :return: all questions answered correctly at least once
    """
    pass

    # for each list of questions:
    #   - take each question, add it to the set of answered questions
    # return the set of answered questions

    answered_questions = set()
    for person in questions:
        for question in person:
            answered_questions.add(question)
    return answered_questions


def split_into_groups(lines: List[str]) -> List[List[str]]:
    """
    Split the list of people's questions into groups, delimited by a blank line
    :param lines: The list of lines
    :return: A list of groups of passengers' questions
    """
    groups = []
    current_group = []
    for line in lines:
        if line == "":
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(line)
    groups.append(current_group)
    return groups


def solve_part1(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        groups = split_into_groups([line.rstrip("\n") for line in input_file.readlines()])
        total = 0
        for group in groups:
            total += len(group_questions_answered(group))
        return total


if __name__ == '__main__':
    print(solve_part1("../inputs/input.txt"))
