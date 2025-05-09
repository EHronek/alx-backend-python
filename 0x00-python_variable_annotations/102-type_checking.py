#!/usr/bin/env python3
"""Type checking"""
from typing import Tuple, List, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # Changed to tuple to match annotation

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed to integer
