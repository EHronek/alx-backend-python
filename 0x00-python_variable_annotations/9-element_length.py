#!/usr/bin/env python3
"""annotates function's parameter and return values with the
appropriate type"""
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """computes the length of a list of sequence"""
    return [(i, len(i)) for i in lst]
