import sys

from trio import sleep

go = None

def balltle():
    '''
    1. 해파리 : 체력 50 나는 체력 150
    1-1. 공격력 : 나는 일반공격 25 해파리는 15
    1-2. 방어 : 방어 시 방어력이 10 상승
    2. 심해 물고기 : 나는 체력 250 물고기 체력 125
    2-1. 공격력 : 물고기 45
    2-2. 방어 : 방어 시 방어력이 25 상승
    3. 보스전(크라켄) : 체력 400 나는 체력 300
    3-1. 공격력 : 크라켄 70
    3-2. 방어 : 방어시 방어력이 50 상승
    '''

def lv_up():
    '''
    1. 첫 레벨업
    1-1.크리스탈 소드 : 방어력이 15 상승, 랜덤 시스템
    1-2. 체력 증가 : 체력이 100 상승 체력 전체 회복
    2. 두번째 레벨업
    2-1.공격력 강화 : 0 ~ 100
    2-2.스탯 강화 : 체력 전체 회복 및 50 상승 방어력 25 상승
    '''

def random_crystal():
    '''
    1. 야바위 게임
    1-1. 규칙 : 돌맹이 5개 중 진짜 크리스탈이 들어있는 돌을 골라야 함 기회 3번
    1-2. 보상 : 연료 크리스탈 

    '''

def read_it():
    '''
    1. 주문외우기
    1-1 방법 : 제시된 거꾸로 된 단어를 올바르게 입력
    1-2 보상 : 연료 크리스탈
    
    '''

def password():
    '''
    1. 비밀번호 입력
    1-1. 방법 : 야구 게임 방식으로 비밀번호 찍기
    1-2. 보상 : 연료 크리스탈
    
    '''

def story():
    
    def typing_Ani(text, speed):
        string = text
        for letter in string: 
            sleep(speed) 
            sys.stdout.write(letter)
            sys.stdout.flush()
        print("") 

    #1.처음
    typing_Ani("로봇기술자 : 난 이게임의 주인공이다.", 0.05)
    typing_Ani("로봇기술자 : 희귀한 광물을 얻으러 출장을 나왔지.", 0.05)
    typing_Ani("로봇기술자 : 이번에 나는 한 심해동굴을 탐사할거야.", 0.05)
    typing_Ani("로봇기술자 : 하지만 이 동굴에는 한번 들어가면 다시 못나온다는 전설이 있던데...", 0.05)
    typing_Ani("로봇기술자 : 아 설마 진짜겠어??.", 0.05)
    typing_Ani("로봇기술자 : 이번에 일 잘하면 승진도 시켜주신다는데 당연히 가야지!!", 0.05)
    typing_Ani("로봇기술자 : 그래도 조금 고민되는데...", 0.05)
    while go != True or go != False:
        go = input("출장을 가시겠습니까? (y/n) :")
        if go == "y":
            typing_Ani("로봇기술자 : 그래 가자!", 0.05)
            go = True
        elif go == "n":
            typing_Ani("로봇기술자 : 혹시 모르니까 가지 말자.", 0.05)
            typing_Ani("상사 : 뭐?? 출장을 안 가?!? 감히 상사의 말을 거역하다니... 넌 해고야!!! ", 0.05)
            go = False
        else:
            typing_Ani("로봇기술자 : 다시 생각해보자.", 0.05)
    
    
    return go
if go == False:
    pass
else:
    story()