import csv
import matplotlib.pyplot as plt

f = open('python_data/csv_data/yp2025.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
yp = []

for row in data:
    yp.append(row)