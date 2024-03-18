#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    A  coroutine that return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency
    """
    result_list: list[float] = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        result = await task
        result_list.append(result)
    return result_list
