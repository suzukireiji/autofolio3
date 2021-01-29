import openpyxl
from openpyxl import chart

def make_piechart():
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

