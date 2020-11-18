import pandas

def csv_to_excel():
    data = pandas.read_csv('autofolio.csv')
    data.to_excel('autofolio.xlsx', encoding='utf-8')