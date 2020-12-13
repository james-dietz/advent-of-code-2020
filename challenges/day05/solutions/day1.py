from challenges.day05 import Seat


def bsp(specifier: str, max_rows: int, max_columns: int) -> Seat:
    """
    Implements the binary space partitioning algorithm.
    :param specifier:   The specification for the requested location
    :param max_rows:    The maximum number of rows
    :param max_columns: The maximum number of columns
    :return: A tuple containing the selected row and column
    """
    pass


def seat_id(seat: Seat) -> int:
    """
    Determine the seat ID based on the row and column.
    seat_id = row * 8 + column
    :param seat: the seat specified by a row and a column
    :return: the seat ID
    """
    pass