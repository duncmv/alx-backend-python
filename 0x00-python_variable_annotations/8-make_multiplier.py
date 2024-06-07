#!/usr/bin/env python3
"""This script creates a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function"""
    def multiply_func(number: float) -> float:
        """Multiplies a float by a multiplier"""
        return number * multiplier
    return multiply_func
