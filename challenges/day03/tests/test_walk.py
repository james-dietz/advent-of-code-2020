import unittest

from challenges.day03.solutions.part1 import trees_encountered


class TestPathWalk(unittest.TestCase):
    input = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

    # take top-left to be (0, 0), +x rightward, +y downward

    def test_walk_knight(self):
        target = 7  # trees encountered on the path
        move = (3, 1)  # 3 right, 1 down
        # move 3 right, 1 down and count the trees
        self.assertEqual(trees_encountered(self.input, move), target)


if __name__ == '__main__':
    unittest.main()
