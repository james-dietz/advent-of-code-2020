import unittest
from typing import Tuple, Set, List

from challenges.day06.solutions.part1 import group_questions_answered

TestCase = Tuple[Tuple[str], Set[str]]


class TestGroupQuestions(unittest.TestCase):
    inputs: List[TestCase] = [
        (("abc"), {"a", "b", "c"}),
        (("a", "b", "c"), {"a", "b", "c"}),
        (("ab", "ac"), {"a", "b", "c"}),
        (("a", "a", "a", "a"), {"a"}),
        (("b"), {"b"})
    ]

    def test_group_questions_answered(self):
        for person_answered, questions in self.inputs:
            self.assertEqual(questions, group_questions_answered(person_answered))


if __name__ == '__main__':
    unittest.main()
