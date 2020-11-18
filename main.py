import csv

from stock_list import Stock_object_list
import stock_price

class Autofolio(object):
    def autofolio_calculate(self):
        name = input('ファイル名を入力して下さい：')
        with open(name, 'w') as autofolio:
            fieldnames = ['ティッカーシンボル', '持株数', '資産額']
            yen = input('現金資産（日本円）を入力して下さい：')
            yen = int(yen)
            dor = input('現金資産（ドル）を入力して下さい：')
            dor = int(dor)
            writer = csv.DictWriter(autofolio, fieldnames=fieldnames)
            writer.writeheader()
            sol = Stock_object_list()
            sol.stock_object_list()
            for i in sol.l:
                writer.writerow({'ティッカーシンボル': i.ticker_synbol,
                                 '持株数': i.stock_number,
                                 '資産額': i.calculate()}
                                )
            writer.writerow({'ティッカーシンボル': '現金',
                             '資産額': dor + (yen / stock_price.exchange())}
                            )