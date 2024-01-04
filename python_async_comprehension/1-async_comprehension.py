#!/usr/bin/env python3
"""
Module with a coroutine that uses async comprehension
to collect and return random numbers from an asynchronous generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator and returns a list of these numbers.
    """
    return [i async for i in async_generator()]
