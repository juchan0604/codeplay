import matplotlib.pyplot as plt
import csv

f = open('python_data/csv_data/10.csv', 'r', encoding='utf-8')
data = csv.reader(f)
result = []
for row in data:
    if '양평읍' in row:
        for i in row[3:]:
            result.append(int(i.replace(',', '')))
        break
            
plt.rc('font', family='Malgun Gothic')