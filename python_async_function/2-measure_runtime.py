#!/usr/bin/env python3
"""
Module to measure the total execution time of the wait_n coroutine
and calculate the average time per execution.
"""

import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per execution.
    """
    start_time = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.monotonic() - start_time
    return total_time / n
