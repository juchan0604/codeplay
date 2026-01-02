import sys
import random

from time import sleep

def typing_Ani(text, speed):
    string = text
    for letter in string: 
        sleep(speed) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("") 


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
    crystal = 0
    typing_Ani('야바위꾼 심해어 : 넌 누구냐?', 0.05)
    typing_Ani('로봇기술자 : 나는 이곳에서 탈출하려는 사람이다.', 0.05)
    typing_Ani('야바위꾼 심해어  : 그려냐? 인간주제에 여기서 어떻게 탈출한다는 거지?', 0.05)
    typing_Ani('로봇기술자 : 이렇게 생긴 걸 모으면 탈출할 수 있어.', 0.05)
    typing_Ani('로봇기술자 : (크리스탈을 보여준다.)', 0.05)
    typing_Ani('야바위꾼 심해어  : 오 마침 나에게 비슷한 게 있는데.', 0.05)
    typing_Ani('야바위꾼 심해어: 그럼 나랑 게임을 해서 이기면 이걸 주지. 기회는 3번', 0.05)
    typing_Ani('로봇기술자 : 알겠어. 한번 불어보자!', 0.05)
    typing_Ani('규칙: 1 ~ 5 중 하나를 고르기', 0.05)
    typing_Ani('하지만 그 중 1개만이 승리입니다.')
    num = 0
    real = 0
    for i in range(3):
        real = random.randint(1, 5)
        num = input('숫자 입력 :')
        if num == real:
            typing_Ani('성공! you win!')
            crystal + 1
            break
        else:
            typing_Ani('실패! try again!')
    
    return crystal
def read_it():
    typing_Ani('돌판 : [여기에 있는 주문을 거꾸로 외워라.]')
    typing_Ani('돌판 : [그러면 하나를 얻을 것이니라.]')
    typing_Ani('로봇기술자 : 이 돌판에 적힌 대로 해 봐야겠어.')
    typing_Ani('규칙 : 제시된 텍스트를 거꾸로 입력하세요.')
    list = ['when_you_collect_all_4_crystals', 'the_door_to_the_boss_room_will_open.',
             'if_you_defeat_that_evil_monster', 'you_will_be_able_to_escape_from_here']
    for i in list:
        print(i[::-1])
def password():
    '''
    1. 비밀번호 입력
    1-1. 방법 : 야구 게임 방식으로 비밀번호 찍기
    1-2. 보상 : 연료 크리스탈
    
    '''

def story():

    #1.처음
    typing_Ani("로봇기술자 : 난 이게임의 주인공이다.", 0.05)
    typing_Ani("로봇기술자 : 희귀한 광물을 얻으러 출장을 나왔지.", 0.05)
    typing_Ani("로봇기술자 : 이번에 나는 한 심해동굴을 탐사할거야.", 0.05)
    typing_Ani("로봇기술자 : 하지만 이 동굴에는 한번 들어가면 다시 못나온다는 전설이 있던데...", 0.05)
    typing_Ani("로봇기술자 : 아 설마 진짜겠어??.", 0.05)
    typing_Ani("로봇기술자 : 이번에 일 잘하면 승진도 시켜주신다는데 당연히 가야지!!", 0.05)
    typing_Ani("로봇기술자 : 그래도 조금 고민되는데...", 0.05)
    typing_Ani("출장을 가시겠습니까? (y/n) :", 0.05)
    # '[가자]를 선택'
    # typing_Ani("로봇기술자 : 함 가보자!", 0.05)
            
    # '[가지 말자]를 선택'
    # typing_Ani("로봇기술자 : 혹시 모르니까 가지 말자.", 0.05)
    # typing_Ani("상사 : 뭐?? 출장을 안 가?!? 감히 상사의 말을 거역하다니... 넌 해고야!!! ", 0.05)
    # '아무것도 고르지 않거나 다른 것을 타이핑한 경우'
    # typing_Ani("로봇기술자 : 다시 생각해보자.", 0.05)
    
story()