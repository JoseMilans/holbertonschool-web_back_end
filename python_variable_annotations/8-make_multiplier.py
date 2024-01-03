#!/usr/bin/env python3
"""
This module provides a type-annotated function make_multiplier that takes a
float multiplier as an argument and returns a function that multiplies a float
by the multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies its input by a given multiplier.
    """
    return lambda j: j * multiplier
