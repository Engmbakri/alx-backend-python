#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a given multiplier.

    Parameters:
    multiplier (float): The multiplier to be used by the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and
    returns its product with the multiplier.
    """
    def multiplier_function(n: float) -> float:
        """
        Multiply the given float by the multiplier.

        Parameters:
        n (float): The float number to be multiplied.

        Returns:
        float: The result of the multiplication.
        """
        return n * multiplier

    return multiplier_function
