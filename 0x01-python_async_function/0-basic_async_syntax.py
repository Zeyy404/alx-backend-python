#!/usr/bin/env python3
"""An asynchronous coroutine module"""
import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    """returns a random delay value"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
