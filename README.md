# ScuffedAPI
Python wrapper for ScuffedAPI.

[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/ScuffedAPI.svg)](https://pypi.org/project/ScuffedAPI/)
[![ScuffedAPI Version: 1.0.3](https://img.shields.io/pypi/v/ScuffedAPI.svg)](https://pypi.org/project/ScuffedAPI/)

## Installing:
Windows: ``py -3 -m pip install ScuffedAPI``<br>
Linux/macOS: ``python3 -m pip install ScuffedAPI``

## Examples:
```
import ScuffedAPI
import asyncio

async def arrow():
    banner = await ScuffedAPI.get_banner(name="Arrow")
    print(banner.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(arrow())
loop.close()
```

This would output:<br>
```StandardBanner1```

fortnitepy example:
```
import fortnitepy
import ScuffedAPI

client = fortnitepy.Client(
    email='example@email.com',
    password='password123'
)

@client.event
async def event_friend_message(message):
    args = message.content.split()
    split = args[1:]
    content = " ".join(split)

    if args[0] == '!playlist':
        playlist = await ScuffedAPI.get_banners(name=content)
        await client.user.party.set_playlist(playlist=playlist.id)
        
client.run()
```

Documentation coming soon, examples of all functions at: https://scuffedapi.herokuapp.com/
