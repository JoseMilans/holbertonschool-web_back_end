#!/usr/bin/env python3
"""
Module to execute multiple instances of task_wait_random concurrently
and return their delays.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with the specified max_delay.
    Returns the list of all the delays in the order they were completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
