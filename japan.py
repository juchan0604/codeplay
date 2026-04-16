
drinks = {'콜라' : [2000, 5, 0], '사이다' : [1500, 10, 0], '물' : [1000, 20, 0], '레쓰비' : [800, 3, 0]}
money = int(input('돈을 넣어주세요.(최소금액 : 800원) :'))

for name, data in drinks.items():
    if money >= data[0]:
        print(f'{name} : {data[0]}원 재고 : {data[1]}')


select = input('음료를 선택해주세요. :')
if drinks[select][1] > 0 and money >= drinks[select][0]:
    money -= drinks[select][0]
    print(f'{select} 나왔습니다. 잔액은 {money}원 입니다.')
    drinks[select][1] -= 1
    drinks[select][2] += 1
    answer = input('더 사시겠습니까?(y/n) :')
    if answer == 'y':
        if money

elif drinks[select][1] == 0:
    print('재고가 소진되었습니다.')
elif money < drinks[select][0]:
    answer = input('돈이 부족합니다. 더 넣으시겠습니까?(y/n) :')
    if answer == 'y':
        money += int(input('돈을 넣어주세요. :'))
    else:
        print(f'거스름돈은 {money}원 입니다.')
        money = 0


