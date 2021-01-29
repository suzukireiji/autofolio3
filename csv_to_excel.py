import pandas
import csv

def csv_to_excel():
    data = pandas.read_csv('autofolio.csv')
    data.to_excel('autofolio.xlsx', encoding='utf-8')

with open('autofolio.csv', 'r') as a:
    reader = csv.DictReader(a)
    for i in reader:
        print(i)
