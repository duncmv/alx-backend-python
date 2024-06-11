#!/usr/bin/env python3
"""async comprehension"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """coroutine will collect 10 random numbers using an async
    comprehensing over the async_generator function
    """
    return [i async for i in async_generator()]
