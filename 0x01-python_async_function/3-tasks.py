#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> str:
    """
    A  coroutine that takes an int and returns an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))