#!/usr/bin/env python3
"""
A module to annotate a give function’s parameters and
return values with the appropriate types
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
