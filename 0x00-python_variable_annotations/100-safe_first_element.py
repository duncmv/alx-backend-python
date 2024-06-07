#!/usr/bin/env python3
"""This script returns the first element of a list"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe annotations for list of any type"""
    if lst:
        return lst[0]
    else:
        return None
