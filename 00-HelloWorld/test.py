#!/usr/bin/env python3

import helloworld
import asyncio
import concurrent


def fn():
    print(helloworld.hello())


async def main():
    print("running")
    executor = concurrent.futures.ThreadPoolExecutor()
    # executor = concurrent.futures.ProcessPoolExecutor()

    print("creating task")
    task = asyncio.create_task(
        asyncio.wait_for(
            asyncio.get_running_loop().run_in_executor(executor, fn),
            timeout=None,
        )
    )
    print("created task")

    while True:
        print("preparing to sleep")
        await asyncio.sleep(1)
        print("finished sleeping")
        if task.done():
            task.result()


asyncio.run(main())
