import asyncio
import time

import aiohttp

from Assignment_4 import generate_urls

urls = generate_urls.urls

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


tasks = []


async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


asyncio.get_event_loop().run_until_complete(main())

print("--- %s seconds ---" % (time.time() - start_time))
