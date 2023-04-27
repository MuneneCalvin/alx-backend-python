#!/usr/bin/env python3
"""Function Annotation Module"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def f(n: float) -> float:
        """
            Multiplies n with the multiplier from the upper function
            and returns the result
        """
        return n * multiplier
    return f
