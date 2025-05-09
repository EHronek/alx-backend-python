#!/usr/bin/env python3

import asyncio

measure_time = __import__('2-measure_runtime').measure_runtime

async def main():
    return await(measure_time())

print(
    asyncio.run(main())
)