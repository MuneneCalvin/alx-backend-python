#!/usr/bin/env python3
"""SumMixedList module with type annotation"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floating point numbers"""
    return sum(mxd_lst)
