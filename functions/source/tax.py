from functions.connections.taxcom import get_taxcom_api
from datetime import datetime, timedelta


async def tax_app(token, data, dt):
    cashbox = {}
    dt_end = datetime.strftime(dt, '%Y-%m-%dT%H:%M:%S')
    dt_start = datetime.strftime((dt - timedelta(days=1)).replace(hour=5), '%Y-%m-%dT%H:%M:%S')
    kkt = await get_taxcom_api('https://api-lk-ofd.taxcom.ru/API/v2/KKTList',
                               token, id=data[1])
    for record in kkt['records']:
        fn = record['fnFactoryNumber']
        shifts = await get_taxcom_api('https://api-lk-ofd.taxcom.ru/API/v2/ShiftList',
                                      token, fn=fn, begin=dt_start, end=dt_end)
        for rec in shifts['records']:
            shift = rec['shiftNumber']
            check = await get_taxcom_api('https://api-lk-ofd.taxcom.ru/API/v2/DocumentList',
                                         token, fn=fn, shift=shift, type=3, begin=dt_start, end=dt_end)
            for r in check['records']:
                cashbox[r['fdNumber']] = r['sum'] / 100
    return cashbox
