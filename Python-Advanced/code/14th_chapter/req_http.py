import requests
import aiohttp
from typing import Any, Dict

JSONObject = Dict[str, Any]

async def http_get(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()

def http_get_sync(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()