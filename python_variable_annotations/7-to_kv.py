#!/usr/bin/env python3
"""
This module provides a type-annotated function to_kv that takes a string k
and an int or float v as arguments, returning a tuple with k and the
square of v as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an int/float value.
    """
    return (k, float(v ** 2))
