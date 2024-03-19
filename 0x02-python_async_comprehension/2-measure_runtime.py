#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime and returns it.
    """
    start_time = time.time()
    tasks = asyncio.gather(async_comprehension(), async_comprehension(),
                           async_comprehension(), async_comprehension())
    await tasks

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time
