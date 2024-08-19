#!/usr/bin/env python3
"""An async routine module"""
from typing import List
import asyncio
import heapq


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns the of all the delays"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return list(heapq.nsmallest(len(delays), delays))
