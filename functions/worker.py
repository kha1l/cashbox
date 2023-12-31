from functions.connections.taxcom import get_token
from database.postgresql import AsyncDatabase
from functions.connections.api import get_units
from configurations.conf import Config
from datetime import datetime, timedelta
from functions.source.sales import sales_app
from functions.source.tax import tax_app
from functions.application import app_check


async def work():
    print('start')
    db = AsyncDatabase()
    cfg = Config()
    pool = await db.create_pool()
    units_dict = cfg.stationary
    token_api = await db.select_tokens(pool)
    units = await get_units(access=token_api['tokenAccess'])
    # dt_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    # dt_end = datetime.strftime(dt_now, '%Y-%m-%dT%H:%M:%S')
    # dt_start = datetime.strftime(dt_now - timedelta(days=2), '%Y-%m-%dT%H:%M:%S')
    dt_now = datetime(2023, 10, 23, 0, 0, 0)
    dt_end = datetime.strftime(dt_now, '%Y-%m-%dT%H:%M:%S')
    dt_start = datetime.strftime(dt_now - timedelta(days=1), '%Y-%m-%dT%H:%M:%S')
    for unit in units:
        if unit['name'] != 'Офис' and unit['name'] in units_dict:
            value = units_dict.get(unit['name'])
            value.append(unit['id'])
            units_dict[unit['name']] = value
    for rest, value in units_dict.items():
        token_tax = await get_token(rest)
        tax = await tax_app(token_tax['sessionToken'], value, dt_now)
        dodo = await sales_app(value[-1], token_api['tokenAccess'], dt_start, dt_end)
        break
    #     await app_check(dodo, tax, token_api['tokenAccess'],
    #                     value[-1], rest, dt_start, dt_end)
    # print(dt_start)
    await pool.close()
