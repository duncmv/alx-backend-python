#!/usr/bin/env python3
"""This script annotates a function"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples"""
    return [(i, len(i)) for i in lst]
