#!/usr/bin/env python3

import helloworld
import asyncio


async def main():
    print("running")

    def fn():
        print(helloworld.hello())

    task = asyncio.create_task(
        asyncio.wait_for(
            asyncio.get_running_loop().run_in_executor(None, fn),
            timeout=None,
        )
    )

    while True:
        print("preparing to sleep")
        await asyncio.sleep(1)
        print("finished sleeping")
        if task.done():
            task.result()


asyncio.run(main())
