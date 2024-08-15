#!/usr/bin/env python3
"""A module to Augment the code with a duck-typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any]:
    """returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
