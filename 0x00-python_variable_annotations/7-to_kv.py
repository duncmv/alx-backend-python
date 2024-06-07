#!/usr/bin/env python3
"""This script returns a kv tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a kv tuple"""
    return (k, v**2)
