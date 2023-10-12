from functions.connections.api import post_api
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from configurations.conf import Config


async def app_check(dodo, tax, token, uuid, name, dt_start, dt_end):
    cfg = Config()
    out_check = {}
    tax_revenue = 0
    dodo_revenue = 0
    dodo_cashbox = {}
    tax_cashbox = {}
    for key, value in dodo.items():
        dodo_revenue += value[-1]
        if value[1] in dodo_cashbox:
            dodo_value = dodo_cashbox.get(value[1])
            total = dodo_value[1] + value[3]
            dodo_cashbox[value[1]] = [value[2], total]
        else:
            dodo_cashbox[value[1]] = [value[2], value[3]]
        check = tax.get(key)
        if check:
            tax_revenue += check
            if value[1] in tax_cashbox:
                tax_value = tax_cashbox.get(value[1])
                total_tax = tax_value[1] + check
                tax_cashbox[value[1]] = [value[2], total_tax]
            else:
                tax_cashbox[value[1]] = [value[2], check]
        else:
            out_check[key] = value
            # if key:
            #     if value[-1] != 0:
            #         out_check[key] = value
    sorted_tax = dict(sorted(tax_cashbox.items(), key=lambda item: item[-1][0]))
    sorted_dodo = dict(sorted(dodo_cashbox.items(), key=lambda item: item[-1][0]))
    new_check_out = {}
    orders_list = []
    result_check = {}
    for key_check, value_check in out_check.items():
        new_check_out[value_check[0]] = int(value_check[-1])
        orders_list.append(value_check[0])
    response = await post_api(f'https://api.dodois.io/dodopizza/ru/production/orders-handover-time',
                              token, units=uuid, _from=dt_start, to=dt_end)
    result = []
    for order in response['ordersHandoverTime']:
        if order['orderId'] in orders_list:
            result_check[order['orderNumber']] = new_check_out[order['orderId']]
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        './configurations/writer.json',
        scopes=scopes
    )
    gsc = gspread.authorize(credentials)
    sh = cfg.table
    sheet = gsc.open_by_key(sh)
    gt = sheet.worksheet(name)
    result.append(dt_start.split('T')[0])
    result.append(int(dodo_revenue))
    rev_dodo = []
    for i in range(1, 4):
        rev = sorted_dodo.get(i)
        if rev:
            result.append(int(rev[-1]))
            rev_dodo.append(int(rev[-1]))
        else:
            result.append(0)
            rev_dodo.append(0)
    result.append(int(tax_revenue))
    rev_tax = []
    for i in range(1, 4):
        rev = sorted_tax.get(i)
        if rev:
            result.append(int(rev[-1]))
            rev_tax.append(int(rev[-1]))
        else:
            result.append(0)
            rev_tax.append(0)
    result.append(int(dodo_revenue - tax_revenue))
    for j in range(3):
        result.append(int(rev_dodo[j] - rev_tax[j]))
    result.append(len(out_check))
    str_check = ''
    for k, v in result_check.items():
        str_check += f'{k} : {v}\n'
    result.append(str_check)
    gt.append_row(result)
