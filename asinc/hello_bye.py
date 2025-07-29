import asyncio


async def hello():
    print('hello')
    await asyncio.sleep(1)
    print(1)


async def bye():
    print('bye')
    await asyncio.sleep(2)
    print(2)


async def main():
    await asyncio.gather(hello(), bye())

asyncio.run(main())
