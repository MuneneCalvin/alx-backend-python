#!/usr/bin/env python3.8
'''
File: 4-tasks.py
'''
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Execute task_wait_random n times and return a list of all random delays
    '''
    delays = []
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    while tasks:
        done, tasks = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delay = await task
            delays.append(delay)
    return delays
