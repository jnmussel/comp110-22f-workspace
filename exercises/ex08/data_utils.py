"""Dictionary related utility functions."""

__author__ = ""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(rows: list[dict[str, str]], name: str) -> list[str]:
    """Produce a list of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in rows:
        result.append(row[str])
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only a fixed number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    if number >= len(table):
        return table
    else:
        for column in table:
            i: int = 0
            the_list: list[str] = []
            while i < number:
                the_list.append(table[column][i])
                i += 1
            result[column] = the_list
        return result


def select(table: dict[str, list[str]], input_list: list[str]) -> dict[str, list[str]]:
    """Docstring for now."""
    result: dict[str, list[str]] = {}
    for item in input_list:
        result[item] = table[item]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines 2 tables into 1."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dict of counting number of occurrences of a str in a list."""
    the_dict: dict[str, int] = {}
    for item in input_list:
        if item in the_dict:
            the_dict[item] += 1
        else:
            the_dict[item] = 1
    return the_dict