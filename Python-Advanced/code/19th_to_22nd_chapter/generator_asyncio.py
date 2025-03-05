import asyncio
from random import randint
from typing import AsyncGenerator, AsyncIterable

from req_http import http_get

MAX_POKEMON = 898

async def get_random_pokemon_name()-> str:
    pokemon_id = randint(1, MAX_POKEMON)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    data = await http_get(url)
    return str(data["name"])

async def next_pokemon(total: int)-> AsyncGenerator[str, None]:
    # sourcery skip: inline-immediately-yielded-variable
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name

async def main():

    async for name in next_pokemon(10):
        print(name)

    names = [name async for name in next_pokemon(10)]
    print(names)

if __name__ == "__main__":
    asyncio.run(main())