#!/usr/bin/env python3.8
'''
File: 0-basic_async_syntax.py
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    function that waits for a random delay between 0 and max_delay
    included and float value seconds and eventually returns ot    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
