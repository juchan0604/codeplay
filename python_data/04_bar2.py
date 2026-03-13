import matplotlib.pyplot as plt
import csv

f = open('python_data/csv_data/mf.csv', 'r', encoding='utf-8')
data = csv.reader(f)

m = []
f = []
result = []
for row in data:
   if "용문" in row[0]:
        # for i in row[3:104]:
        #     m.append(-(int(i)))
        # for i in row[106:]:
        #     f.append(int(i))
        for i in range(101):
            m.append(-int(row[(i+3)]))
            f.insert(0, int(row[-(i+1)]))
        break
   
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=150)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('양평군 용문면 성별분포')
plt.barh(range(101), m, label = '남성')
plt.barh(range(101), f, label = '여성')
plt.legend()
plt.show()