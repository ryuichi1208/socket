import asyncio


Seconds = [
    ("first", 5),
    ("second", 0),
    ("third", 3)
]


async def sleeping(order, seconds, hook=None):
    await asyncio.sleep(seconds)
    if hook:
        hook(order)
    return order


async def basic_async(num):
    # the order of result is nonsequential (not depends on order, even sleeping time)
    for s in Seconds:
        r = await sleeping(*s)
        print("{0}'s {1} is finished.".format(num, r))
    return True


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # make two tasks in event loop
    asyncio.ensure_future(basic_async(1))
    asyncio.ensure_future(basic_async(2))
    loop.run_forever()
