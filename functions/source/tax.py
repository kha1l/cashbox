from functions.connections.taxcom import get_taxcom_api
from datetime import datetime, timedelta

class Tax:
    cashbox = {}
    total_count = 0

    async def tax_app(self, token, data, dt):
        dt_end = datetime.strftime(dt, '%Y-%m-%dT%H:%M:%S')
        dt_start = datetime.strftime((dt - timedelta(days=1)).replace(hour=5), '%Y-%m-%dT%H:%M:%S')
        kkt = await get_taxcom_api('https://api-lk-ofd.taxcom.ru/API/v2/KKTList',
                                   token, id=data[2])
        for record in kkt['records']:
            fn = record['fnFactoryNumber']
            shifts = await get_taxcom_api('https://api-lk-ofd.taxcom.ru/API/v2/ShiftList',
                                          token, fn=fn, begin=dt_start, end=dt_end)
            for rec in shifts['records']:
                shift = rec['shiftNumber']
                check = await get_taxcom_api('https://api-lk-ofd.taxcom.ru/API/v2/DocumentList',
                                             token, fn=fn, shift=shift, type=3, begin=dt_start, end=dt_end)
                count = check['counts']
                self.total_count += count['recordCount']
                for r in check['records']:
                    self.cashbox[r['fdNumber']] = r['sum'] / 100
