from functions.connections.taxcom import get_token
from database.postgresql import AsyncDatabase
from functions.connections.api import get_units
from configurations.conf import Config
from datetime import datetime, timedelta
from functions.source.sales import Sales
from functions.source.tax import Tax


async def work():
    db = AsyncDatabase()
    cfg = Config()
    pool = await db.create_pool()
    token_tax = await get_token()
    units_dict = cfg.stationary
    token_api = await db.select_tokens(pool)
    units = await get_units(access=token_api['tokenAccess'])
    dt_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    dt_end = datetime.strftime(dt_now, '%Y-%m-%dT%H:%M:%S')
    dt_start = datetime.strftime(dt_now - timedelta(days=1), '%Y-%m-%dT%H:%M:%S')
    for unit in units:
        if unit['name'] != 'Офис' and unit['name'] in units_dict:
            value = units_dict.get(unit['name'])
            value.append(unit['id'])
            units_dict[unit['name']] = value
    for rest, value in units_dict.items():
        sales = Sales()
        await sales.sales_app(value[-1], token_api['tokenAccess'], dt_start, dt_end)
        print(sales.cashbox)
        break
    await pool.close()
