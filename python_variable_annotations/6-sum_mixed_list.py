#!/usr/bin/env python3
"""
This module provides a type-annotated function sum_mixed_list that takes a list
of integers and floats mxd_lst as an argument and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Compute the sum of a mixed list of integers and floats.
    """
    return sum(mxd_lst)
