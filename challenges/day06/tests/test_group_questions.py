import unittest
from typing import Tuple, Set, List

from challenges.day06.solutions.part1 import group_questions_answered
from challenges.day06.solutions.part2 import group_questions_all_answered

TestCase = Tuple[Tuple[str], Set[str], Set[str]]


class TestGroupQuestions(unittest.TestCase):
    inputs: List[TestCase] = [
        (("abc"), {"a", "b", "c"}, {"a", "b", "c"}),
        (("a", "b", "c"), {"a", "b", "c"}, {}),
        (("ab", "ac"), {"a", "b", "c"}, {"a"}),
        (("a", "a", "a", "a"), {"a"}, {"a"}),
        (("b"), {"b"}, {"b"})
    ]

    def test_group_questions_answered(self):
        for person_answered, questions, _ in self.inputs:
            self.assertEqual(questions, group_questions_answered(person_answered))

    def test_group_questions_all_answered(self):
        for person_answered, _, questions in self.inputs:
            self.assertEqual(questions, group_questions_all_answered(person_answered))


if __name__ == '__main__':
    unittest.main()
