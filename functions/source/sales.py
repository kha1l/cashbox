from functions.connections.api import post_api


async def sales_app(rest, token, dt_start, dt_end):
    skip = 0
    take = 1000
    cashbox = {}
    reach = True
    while reach:
        response = await post_api(f'https://api.dodois.io/dodopizza/ru/accounting/sales',
                                  token, units=rest, _from=dt_start, to=dt_end,
                                  skip=skip, take=take)
        skip += take
        for sales in response['sales']:
            products = sales['products']
            order = sales['orderId']
            cashbox_type = sales['cashBoxType']
            cashbox_number = sales['cashBoxNumber']
            check = sales['checkNumber']
            price = 0
            for pr in products:
                price += pr['priceWithDiscount']
                cashbox[check] = [order, cashbox_number, cashbox_type, price]
        try:
            if response['isEndOfListReached']:
                reach = False
        except TypeError:
            reach = False
        except KeyError:
            reach = False
    return cashbox
