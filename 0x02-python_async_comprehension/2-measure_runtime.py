#!/usr/bin/env python3
"""measure runtime"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return (end - start)
