#!/usr/bin/env python3
"""Ducktyping Iterables Module"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, containing the individual elements
    of an iterable object and their respective length
    """
    return [(i, len(i)) for i in lst]
