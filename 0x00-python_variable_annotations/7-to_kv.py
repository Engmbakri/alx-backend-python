#!/usr/bin/env python3
"""
module contains a function to create a tuple from a string and the
square of an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int or float.

    Parameters:
    k (str): The string.
    v (Union[int, float]): The int or float number.

    Returns:
    Tuple[str, float]: tuple where the first element is the string k
    and the second element is the square of v.
    """
    return (k, float(v ** 2))
