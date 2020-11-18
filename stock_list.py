import stock_price

stock_list = {
    'spxl': 466,
    'zi': 54,
    'docu': 5,
    'fb': 4,
    'plug': 95,
    'rprx': 23,
    'shop': 1,
    'tsla': 3
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