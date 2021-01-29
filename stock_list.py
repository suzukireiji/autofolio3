import stock_price

stock_list = {
    'spxl': 493,
    'zi': 54,
    'plug': 95,
    'rprx': 42,
    'gdrx': 58,
    'ai': 15
}

class Stock_object_list(object):
    def __init__(self):
        self.l = []

    def stock_object_list(self):
        for k, v in stock_list.items():
            k = stock_price.Stock_price(k, v)
            self.l.append(k)

if __name__ == '__main__':
    sol = Stock_object_list()
    sol.stock_object_list()
    print(sol.l[0].calculate())