#!/usr/bin/env python3
"""This sript sums up a list of integers and floats"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """Returns sum of a list of integers and floats"""
    return sum(input_list)
