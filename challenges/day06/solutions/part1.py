from typing import Tuple, Set


def group_questions_answered(questions: Tuple[str]) -> Set[str]:
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