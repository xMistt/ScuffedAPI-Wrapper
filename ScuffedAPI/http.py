import aiohttp
import sys
import asyncio
import logging

logging.getLogger('asyncio').setLevel(logging.CRITICAL)

class HTTPClient:
    def __init__(self, connector=None):
        self.connector = connector

    async def request(self, url, method):
        async with aiohttp.ClientSession() as session:
            async with session.request(method=method, url=url) as r:
                return await r.json()

    async def scuffedapi_request(self, url):
        return await self.request(method='GET', url=url)

    def get_event_loop(self):
        if sys.platform == 'win32':
            policy = asyncio.get_event_loop_policy()
            loop = policy._local._loop

            if loop is None:
                selector = selectors.SelectSelector()
                loop = asyncio.SelectorEventLoop(selector)
                asyncio.set_event_loop(loop)
            
            elif isinstance(loop, asyncio.ProactorEventLoop):
                raise RuntimeError('asyncio.ProactorEventLoop is not supported')
        
        else:
            loop = asyncio.get_event_loop()

        return loop
