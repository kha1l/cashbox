from .api import post_api


class Sales:
    skip = 0
    take = 1000
    cashbox = {}

    async def sales_app(self, rest, token, dt_start, dt_end):
        reach = True
        while reach:
            response = await post_api(f'https://api.dodois.io/dodopizza/ru/accounting/sales',
                                      token, units='000d3a240c719a8711e68aba13f8c13f', _from=dt_start, to=dt_end,
                                      skip=self.skip, take=self.take)
            self.skip += self.take
            for sales in response['sales']:
                products = sales['products']

                for pr in products:
                    if pr['pizzaHalves']:
                        print(sales)

                products = sales['products']
                channel = sales['salesChannel']
                order = sales['orderSource']
            try:
                if response['isEndOfListReached']:
                    reach = True
            except TypeError:
                reach = True
            except KeyError:
                reach = True
