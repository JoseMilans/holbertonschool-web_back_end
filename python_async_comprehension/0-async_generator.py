#!/usr/bin/env python3
"""
Module with an asynchronous generator coroutine that loops 10 times,
each time asynchronously waits for 1 second, then yields a random
number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator that yields a random number between 0 and 10
    after waiting for 1 sec for each of 10 iterations.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
