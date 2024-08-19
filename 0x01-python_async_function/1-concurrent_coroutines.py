#!/usr/bin/env python3
"""An async routine module"""
from typing import List
import asyncio
import heapq


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns the of all the delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return list(heapq.nsmallest(len(delays), delays))
