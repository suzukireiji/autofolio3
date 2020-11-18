import pandas_datareader as pnd
from datetime import datetime, date, timedelta

class Stock_price(object):

    def __init__(self, t, s):
        self.ticker_synbol = t
        self.stock_number = s

    def calculate(self):
        lastday = datetime.today()
        finish = False
        while finish == False:
            try:
                stock = pnd.DataReader(self.ticker_synbol, "yahoo", lastday)
                finish = True
            except KeyError:
                lastday -= timedelta(days=1)
            except ValueError:
                lastday -= timedelta(days=1)
        return stock["Close"][0] * self.stock_number

    def change(self, s):
        self.stock_number = s

def exchange():
    lastday = datetime.today()
    finish = False
    while finish == False:
        try:
            exchange = pnd.DataReader('JPY=X', "yahoo", lastday)
            finish = True
        except KeyError:
            lastday -= timedelta(days=1)
        except ValueError:
            lastday -= timedelta(days=1)
    return exchange["Close"][0]


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


if __name__ == '__main__':
    print(exchange())
    for k, v in stock_list.items():
        k = Stock_price(k, v)
        print(k.calculate())