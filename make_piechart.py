import openpyxl
from openpyxl import chart

wb = openpyxl.load_workbook('autofolio.xlsx')
ws = wb.worksheets[0]

piechart = chart.PieChart()

values = chart.Reference(ws,
              min_row=1, min_col=4,
              max_row=10, max_col=4)
piechart.add_data(values, titles_from_data=True)

xvalues = chart.Reference(ws,
              min_row=2, min_col=2,
              max_row=10, max_col=2)
piechart.set_categories(xvalues)

ws.add_chart(piechart, 'G2')
wb.save('autofolio.xlsx')

