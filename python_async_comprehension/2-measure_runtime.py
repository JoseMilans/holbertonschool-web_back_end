#!/usr/bin/env python3
"""
Module with a coroutine that measures the runtime
of executing async_comprehension four times simultaneously.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = time.monotonic()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.monotonic()
    return end_time - start_time
