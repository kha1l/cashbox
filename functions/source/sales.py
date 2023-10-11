from functions.connections.api import post_api


class Sales:
    skip = 0
    take = 1000
    cashbox = {}

    async def sales_app(self, rest, token, dt_start, dt_end):
        reach = True
        while reach:
            response = await post_api(f'https://api.dodois.io/dodopizza/ru/accounting/sales',
                                      token, units=rest, _from=dt_start, to=dt_end,
                                      skip=self.skip, take=self.take)
            self.skip += self.take
            for sales in response['sales']:
                products = sales['products']
                cashbox_type = sales['cashBoxType']
                cashbox_number = sales['cashBoxNumber']
                check = sales['checkNumber']
                price = 0
                for pr in products:
                    price += pr['priceWithDiscount']
                self.cashbox[check] = [cashbox_number, cashbox_type, price]
            try:
                if response['isEndOfListReached']:
                    reach = False
            except TypeError as e:
                print(e)
                reach = False
            except KeyError as e:
                print(e)
                reach = False
