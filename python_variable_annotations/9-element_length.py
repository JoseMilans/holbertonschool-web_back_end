#!/usr/bin/env python3
"""
This module provides a type-annotated function element_length which takes an
iterable of sequences lst as an argument and returns a list of tuples with each
sequence and its corresponding length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
