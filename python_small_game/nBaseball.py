import random
import os

def cl():
    os.system("cls")

num = ""
guess = ""
count = 0
log = []

def make_num():
    num_temp = ""
    num_temp += str(random.randint(0, 9))
    while len(num_temp) < 3:
        temp = str(random.randint(0, 9))
        if temp not in num_temp:
            num_temp += temp

    return num_temp

def gues_num(n):
    global guess
    global log
    global count

    while n != guess:
        strike = 0
        ball = 0
        result = ""
        guess = input('비밀숫자는 뭘까?= > ')
        

        for i in range(len(guess)):
            if guess[i] in n:
                if guess[i] == n[i]:
                    strike += 1
                else:
                    ball += 1
        if strike + ball == 0:
            result = f"{guess} - 아웃"
        else:
            if strike > 0 and ball > 0:
                result = f"{guess} - {strike}s {ball}b"
            else:
                if strike > 0:
                    result = f"{guess} - {strike}s"
                else:
                    result = f"{guess} - {ball}b"
        log.append(result)
        count += 1
        
        cl()
        for i in log:
            print(i)
    
    return count

def final(n, c):
    print("수고했다.")
    print(f"정답은 {n}이다.")
    print(f"너는 {c}번만에 맞췄군.")
    if count < 5:
        print("또 찍었지 이 도박쟁이")
    elif count < 10:
        print("잘했다")
    else:
        print("you are an idiot hahahahahahaha ahahahaha")
def game():
    global num
    global count

    num = make_num()
    count = gues_num(num)
    final(num, count)

game()