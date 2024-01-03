#!/usr/bin/env python3
"""
This module provides a type-annotated function sum_list that takes a list of
floats as an argument input_list and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Compute the sum of a list of floats
    """
    return sum(input_list)
