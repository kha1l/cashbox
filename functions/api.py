import aiohttp
from aiohttp.client_exceptions import ContentTypeError
import asyncio


async def post_api(url, access, **kwargs) -> dict:
    data = {}
    retry_limit = 5
    retry_delay = 60
    for key, value in kwargs.items():
        if key == '_from':
            data['from'] = value
        else:
            data[key] = value
    headers = {
        "user-agent": 'DodoSouth',
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {access}"
    }
    async with aiohttp.ClientSession(trust_env=True) as session:
        for i in range(retry_limit):
            async with session.get(url, headers=headers, params=data) as response:
                try:
                    if response.status == 200:
                        response = await response.json()
                        return response
                    elif response.status == 429 or response.status == 503 or response.status == 500 \
                            or response.status == 502:
                        await asyncio.sleep(retry_delay)
                    else:
                        print(await response.json())
                        break
                except ContentTypeError:
                    print(response.content)
                    return {}
        return {}


async def get_units(**kwargs) -> dict:
    headers = {
        "user-agent": "DodoSouth",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {kwargs['access']}"
    }
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('https://api.dodois.io/auth/roles/units',
                               headers=headers) as response:
            try:
                response = await response.json()
                return response
            except ContentTypeError:
                return {}
