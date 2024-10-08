#!/usr/bin/env python3
"""A coroutine called `async_comprehension` that takes no arguments module"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers using an async comprehensing
    over `async_generator`, then return the 10 random numbers.
    """
    return [num async for num in async_generator()]
