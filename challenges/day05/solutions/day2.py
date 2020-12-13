from challenges.day05.solutions.day1 import bsp, seat_id


def solve_day2(input_filename: str) -> int:
    with open(input_filename, "r") as input_file:
        # get the list of seat specifiers
        seat_specifiers = [line.rstrip("\n") for line in input_file.readlines()]
        # resolve specifiers to seats (row, column)
        seats = map(lambda seat_specifier: bsp(seat_specifier, 128, 8), seat_specifiers)
        sorted_seat_ids = set(sorted(list(map(lambda seat: seat_id(seat), seats))))
        # find the seat manually, it's the only one in the range
        print(set(range(1000)).difference(sorted_seat_ids))


if __name__ == '__main__':
    print(solve_day2("../inputs/input.txt"))
