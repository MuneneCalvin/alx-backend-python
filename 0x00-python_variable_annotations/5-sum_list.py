#!/usr/bin/env python3
"""SumList module with type annotation"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floating point numbers"""
    return sum(input_list)
