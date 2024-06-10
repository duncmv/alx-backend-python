#!/usr/bin/env python3
"""concurrent coroutines"""
import asyncio
from typing import List


task = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a function that spawns task_wait_random n times
    """
    delays = await asyncio.gather(*[task(max_delay) for _ in range(n)])
    return sorted(delays)
