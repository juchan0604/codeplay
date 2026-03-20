import matplotlib.pyplot as plt
import csv

f = open('python_data/csv_data/mf.csv', 'r', encoding='utf-8')
data = csv.reader(f)
data2 = []
for i in data:
    data2.append(i)
data = 0
f.close()

running = True

while running:
    answer = input('지역명을 입력해주세요 (종료하려면 q 입력): ')

    m = []
    f = []
    go = False
    result = []

    if answer == 'q':
        running = False
    else:
        for row in data2:
            if answer in row[0]:
                go = True
                for i in range(101):
                    m.append(-int(row[(i+3)]))
                    f.insert(0, int(row[-(i+1)]))
                break

        if go:
            plt.style.use('ggplot')
            plt.figure(figsize=(10, 5), dpi=150)
            plt.rc('font', family='Malgun Gothic')
            plt.rcParams['axes.unicode_minus'] = False
            plt.title(f'양평군 {answer} 성별분포')
            plt.barh(range(101), m, label = '남성')
            plt.barh(range(101), f, label = '여성')
            plt.legend()
            plt.show()
        else:
            print('해당 지역이 없습니다. 다시 입력해주세요.')