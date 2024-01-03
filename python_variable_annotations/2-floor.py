#!/usr/bin/env python3
"""
This module provides a type-annotated function floor that takes a float
argument n and returns the floor of the float as an integer.
"""

import math


def floor(n: float) -> int:
    """Compute the floor of a float and return it as an int.
    """
    return math.floor(n)
