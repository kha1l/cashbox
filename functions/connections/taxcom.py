import aiohttp
from aiohttp.client_exceptions import ContentTypeError
from configurations.conf import Config

async def get_token():
    cfg = Config()
    data = {
        'login': cfg.login,
        'password': cfg.password_tax
    }
    headers = {
        "user-agent": 'DodoSouth',
        "Content-Type": "application/json",
        "Integrator-ID": cfg.id
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api-lk-ofd.taxcom.ru/API/v2/Login',
                                headers=headers, json=data) as response:
            try:
                response = await response.json()
                return response
            except ContentTypeError:
                return {}


async def get_taxcom_api(url, access, **kwargs):
    data = {}
    for key, value in kwargs.items():
        data[key] = value
    headers = {
        "user-agent": 'DodoSouth',
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=data) as response:
            try:
                response = await response.json()
                return response
            except ContentTypeError:
                return {}
