#!/usr/bin/env python3
"""
async coroutine wait_n that takes in 2 int arguments
 n and max_delay
spawn wait_random n times with
the specified max_delay.
wait_n returns the list of all
the delays  in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delays in ascending order
    """
    delays = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]