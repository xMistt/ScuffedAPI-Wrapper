import ScuffedAPI
import asyncio

async def arrow():
    banner = await ScuffedAPI.get_banners(name="Arrow")
    print(banners.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(arrow())
loop.close()
