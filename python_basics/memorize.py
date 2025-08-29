import random
eng = ['apple', 'grape', 'peach', 'pear', 'watermelon' ]
kor = ['사과', '포도', '복숭아', '배','수박']

order = 0
end = 0
def exercise():
    score = 0
    for i in range(len(eng)):
        text = input(f'{kor[i]} 영어입력:')
        if text == eng[i]:
            print('딩동댕~')
            score += 1
        else:
            print('틀렸죠 메롱~')
    print(f'니 점수는 {score}/{len(kor)}점이다 인석아~')

def add():
    k = input('단어추가 한국어:')
    e = input('단어추가 영어:')
    c = input(f'정말 추가하시겠습니까? Y/N:')
    if c.upper() == 'Y':
        kor.append(k)
        eng.append(e)
        print('(추가완료)')
    else:
        print('(취소됨)')

while end == 0:
    a = input('1.시험 2.추가 3.종료:')
    if a == '1':
        exercise()
    elif a == '2':
        add()
    elif a == '3':
        end = 1
    else:
        print('재입력')



