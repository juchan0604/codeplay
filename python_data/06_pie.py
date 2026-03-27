import matplotlib.pyplot as plt

# plt.pie([10, 20])

# size = [2441, 2312, 1031, 1233]
# plt.axis('equal')
# plt.pie(size)

# plt.rc('font', family='Malgun Gothic')
# size = [2441, 2312, 1031, 1233, 555]
# label = ['A형', 'B형', 'O형', 'AB형', '우리형']
# plt.axis('equal')
# plt.pie(size, labels=label)

# plt.rc('font', family='Gulim')
# size = [1125, 2312, 1031, 1233]
# label = ['typeA', 'typeB', '에이삐형', 'typeO']

plt.rc('font', family='Gulim')
blood = [3141, 2612, 1031, 2733]
label = ['A형', 'B형', 'AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']

ddi = [5432, 4321, 3210, 6974, 5252, 6767, 4456, 7543, 9865, 3494, 7593, 9999]
label2 = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8))

axes[0].pie(blood, explode=(0.1, 0.01, 0.01, 0.01), labels=label, autopct='%.1f%%')
axes[0].set_title('혈액형')

axes[1].pie(ddi, explode=(0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01), labels=label2, autopct='%.1f%%')
axes[1].set_title('띠')

# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.1f%%')
# plt.legend()

# plt.axis('equal')
# plt.pie(size, explode=(0,0,0,0.2), labels=label, autopct='%.1f%%', colors=color)
# plt.legend()


plt.show()