#!/usr/bin/env python3
"""Module for safely accessing the first element in a sequence using typing."""

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists, otherwise return None.

    Args:
        lst (Sequence[Any]): The sequence to check.

    Returns:
        Union[Any, None]: The first element or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

