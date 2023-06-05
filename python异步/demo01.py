# import asyncio
#
#
# async def main():
#     print('one')
#     await asyncio.sleep(1)
#     print('two')
#
#
# asyncio.run(main())

# !/usr/bin/env python3
# async.py

import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


asyncio.run(main())

print('succeed!')
