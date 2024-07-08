#!/usr/bin/env python3
"""
This module contains a single coroutine wait_random which waits for
a random delay between 0 and max_delay seconds and returns the delay.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum delay to wait. Default is 10.

    Returns:
        float: The actual delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
