#!/usr/bin/env python3
"""complex types -functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function"""
    return lambda x: x * multiplier
