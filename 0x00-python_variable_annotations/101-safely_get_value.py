#!/usr/bin/env python3
"""This script annotates a function"""
from typing import TypeVar, Mapping, Union, Any


T = TypeVar('T', int, float)


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safe annotations for dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
