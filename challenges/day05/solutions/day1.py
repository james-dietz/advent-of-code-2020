from math import floor, ceil, log

from challenges.day05 import Seat


LOWER_HALF = "FL"
UPPER_HALF = "BR"

def bsp(specifier: str, max_rows: int, max_columns: int) -> Seat:
    """
    Implements the binary space partitioning algorithm.
    :param specifier:   The specification for the requested location
    :param max_rows:    The maximum number of rows
    :param max_columns: The maximum number of columns
    :return: A tuple containing the selected row and column
    """
    low_row, high_row = 0, max_rows - 1
    low_column, high_column = 0, max_columns - 1

    # split the specifier in two by row or column
    row_splits = specifier[:floor(log(max_rows, 2))]
    column_splits = specifier[-floor(log(max_columns, 2)):]

    # get the row and column
    row = split(row_splits, low_row, high_row)
    column = split(column_splits, low_column, high_column)

    return row, column


def split(specifier: str, low: int, high: int) -> int:
    for char in specifier[:-1]:
        # take the lower half
        if char in LOWER_HALF:
            high = floor(high - ((high - low) / 2))
        # take the upper half
        elif char in UPPER_HALF:
            low = ceil(low + ((high - low) / 2))

    # for the final split, take the low or high number
    return low if specifier[-1] in "FL" else high


def seat_id(seat: Seat) -> int:
    """
    Determine the seat ID based on the row and column.
    seat_id = row * 8 + column
    :param seat: the seat specified by a row and a column
    :return: the seat ID
    """
    row, column = seat
    return row * 8 + column
