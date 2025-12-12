import asyncio


async def async_map(func, data):
tasks = [asyncio.to_thread(func, x) for x in data]
return await asyncio.gather(*tasks)
