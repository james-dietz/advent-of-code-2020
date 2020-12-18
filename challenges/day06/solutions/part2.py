from typing import Tuple, Set


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
