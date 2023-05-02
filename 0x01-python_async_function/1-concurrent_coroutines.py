#!/usr/bin/env python3.8
'''
File: 1-concurrent_coroutines.py
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Generate a list of `n` random delays between 0 and `max_delay`
    using asyncio.sleep() and return the list in ascending order.
    '''
    delays = []
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    while tasks:
        done, tasks = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delay = await task
            delays.append(delay)
    return delays
