import csv
import pandas
import openpyxl
from openpyxl import chart

from stock_list import Stock_object_list
import stock_price

class Autofolio(object):

    def __init__(self, name=input('ファイル名を入力して下さい：')):
        self.name = name

    def autofolio_calculate(self):
        with open(self.name + '.csv', 'w') as autofolio:
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

    def csv_to_excel(self):
        data = pandas.read_csv(self.name + '.csv')
        data.to_excel(self.name + '.xlsx', encoding='utf-8')

    def make_piechart(self):
        wb = openpyxl.load_workbook(self.name + '.xlsx')
        ws = wb.worksheets[0]

        piechart = chart.PieChart()

        values = chart.Reference(ws,
                                 min_row=1, min_col=4,
                                 max_row=100, max_col=4)
        piechart.add_data(values, titles_from_data=True)

        xvalues = chart.Reference(ws,
                                  min_row=2, min_col=2,
                                  max_row=100, max_col=2)
        piechart.set_categories(xvalues)

        ws.add_chart(piechart, 'G2')
        wb.save(self.name + '.xlsx')


pf = Autofolio()
pf.autofolio_calculate()
pf.csv_to_excel()
pf.make_piechart()
