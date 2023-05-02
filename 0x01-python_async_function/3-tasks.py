#!/usr/bin/env python3.8
'''
File: 3-tasks.py
'''
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    takes an integer max_delay and returns an asyncio task
    '''
    my_task = asyncio.create_task(wait_random(max_delay))
    return my_task
