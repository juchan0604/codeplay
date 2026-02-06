import sys
import random

from time import sleep

crystal = 0

def typing_Ani(text, speed):
    string = text
    for letter in string: 
        sleep(speed) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("") 


def battle_1():
    typing_Ani('로봇기술자 : 저건 뭐지?', 0.05)
    typing_Ani('로봇기술자 : 해파리네.', 0.05)
    typing_Ani('로봇기술자 : 맛있겠다.', 0.05)
    typing_Ani('로봇기술자 : 잡아서 해파리냉채로 만들어 먹어야쥐^^', 0.05)
    typing_Ani('공지 : 공격을 하고 3분의 1로 공격을 피할 수 있습네다.', 0.05)
    typing_Ani('전투 시작', 0.05)
    hp = 150
    enemy_hp = 50
    attack = 25
    enemy_attack = 15
    block = 10
    on = 0
    answer = 0
    run = 0
    while hp > 0 and enemy_hp > 0:
        run = random.randint(1, 3)
        typing_Ani(f'해파리 체력 : {enemy_hp}, 내 체력 : {hp}', 0.05)
        action = input('행동 선택 (1.공격 2.방어) : ')
        if action == '1':
            typing_Ani(f'공격했다! 해파리는 {attack}데미지를 입었다.', 0.05)
            enemy_hp -= attack
        elif action == '2':
            typing_Ani(f'이번 턴은 방어한다! {block} 만큼 방어력이 올랐다.', 0.05)
            on = 1
        if on == 1:
            typing_Ani(f'적이 공격했지만 방어했다. {enemy_attack - block} 데미지를 입었다.', 0.05)
            hp -= (enemy_attack - block)
            on = 0
        else:
            answer = input('피할 곳을 선택하세요 (1 ~ 3) :')
            if answer == run:
                typing_Ani('공격을 회피했다!', 0.05)
            else:
                typing_Ani(f'적이 공격했다. {enemy_attack} 데미지를 입었다.', 0.05)
                hp -= enemy_attack
    if hp <= 0:
        typing_Ani('사망', 0.05)
    elif enemy_hp <= 0:
        typing_Ani('승리했다.', 0.05)
def battle_2():   
    
    #2. 심해 물고기 : 나는 체력 250 물고기 체력 200 , 공격력 : 물고기 45 , 방어 : 방어 시 방어력이 25 상승
    typing_Ani('심해어 : 친입자다. 못생겼다.', 0.05)
    typing_Ani('심해어 : 죽이겠다!!!', 0.05)
    typing_Ani('로봇기술자 : ?', 0.05)
    typing_Ani('로봇기술자 : 니 나한테 잡히면 죽는다', 0.05)
    typing_Ani('로봇기술자 : 나 해병대 나왔다 아이가', 0.05)
    typing_Ani('공지 : 크리스탈 소드를 얻어 최대 공격력이 오르는 대신 데미지가 0 ~ 70 까지 랜덤입네다.', 0.05)
    typing_Ani('공지 : 해파리 냉채를 먹어 그 외 능력치도 올랐습네다.', 0.05)
    typing_Ani('전투 시작', 0.05)
    
    hp = 250
    enemy_hp = 125
    attack = 0
    enemy_attack = 45
    block = 25
    on = 0
    run = 0
    answer = 0
    while hp > 0 and enemy_hp > 0:
        attack = random.randint(0, 70)
        run = random.randint(1, 3)
        typing_Ani(f'심해어 체력 : {enemy_hp}, 내 체력 : {hp}, 이번 턴 공격력 : {attack}', 0.05)
        action = input('행동 선택 (1.공격 2.방어) : ')
        if action == '1':
            typing_Ani(f'공격했다! 심해어는 {attack}데미지를 입었다.', 0.05)
            enemy_hp -= attack
        elif action == '2':
            typing_Ani(f'이번 턴은 방어한다! {block} 만큼 방어력이 올랐다.', 0.05)
            on = 1
        if on == 1:
            typing_Ani(f'적이 공격했지만 방어했다. {enemy_attack - block} 데미지를 입었다.', 0.05)
            hp -= (enemy_attack - block)
            on = 0
        else:
            answer = input('피할 곳을 선택하세요 (1 ~ 3) :')
            if answer == run:
                typing_Ani('공격을 회피했다!', 0.05)
            else:
                typing_Ani(f'적이 공격했다. {enemy_attack} 데미지를 입었다.', 0.05)
                hp -= enemy_attack
    if hp <= 0:
        typing_Ani('사망', 0.05)
    elif enemy_hp <= 0:
        typing_Ani('승리했다.', 0.05)

def boss():
    #3. 보스전(크라켄) : 체력 400 나는 체력 300 , 공격력 : 크라켄 70 , 방어 : 방어시 방어력이 50 상승
    typing_Ani('??? : 인간주제에 여기까지 오다니 흥미롤구나...', 0.05)
    typing_Ani('로봇기술자 : 뭐야 이 타코야끼같이 생긴 놈은?', 0.05)
    typing_Ani('로봇기술자 : 닌 뭐냐?', 0.05)
    typing_Ani('??? : 감히 이 몸을 타코야끼라고!!!', 0.05)
    typing_Ani('크라켄 : 이 몸으로 말하면 위대한 동굴의 왕 크라켄이다!', 0.05)
    typing_Ani('로봇기술자 : 니가? ㅋ', 0.05)
    typing_Ani('로봇기술자 ; 니가 크라켄이면 나는 메갈로돈이다', 0.05)
    typing_Ani('크라켄 : 진짜 인간주제에...', 0.05)
    typing_Ani('크라켄 : 잡담도 여기서 끝이다.', 0.05)
    typing_Ani('크라켄 : 그만 죽어라!', 0.05)
    typing_Ani('로봇기술자 : 이렇게 된 이상 싸우자')
    typing_Ani('공지 : 두번째 레벨업을 통해 공격력이 0 ~ 100 까지 올랐습네다.', 0.05)
    typing_Ani('공지 : 심해어 회를 썰어 먹어 기타 능력치도 상승했습네다.', 0.05)
    typing_Ani('공지..? : 그럼 행우ㄴ을 빕ㄴ...', 0.05)
    typing_Ani('!보스전!', 0.05)
    hp = 300
    enemy_hp = 400
    attack = 0
    enemy_attack = 70
    block = 50
    on = 0
    run = 0
    answer = 0
    while hp > 0 and enemy_hp > 0:
        attack = random.randint(0, 100)
        run = random.randint(1, 3)
        typing_Ani(f'심해어 체력 : {enemy_hp}, 내 체력 : {hp}, 이번 턴 공격력 : {attack}', 0.05)
        action = input('행동 선택 (1.공격 2.방어) : ')
        if action == '1':
            typing_Ani(f'공격했다! 심해어는 {attack}데미지를 입었다.', 0.05)
            enemy_hp -= attack
        elif action == '2':
            typing_Ani(f'이번 턴은 방어한다! {block} 만큼 방어력이 올랐다.', 0.05)
            on = 1
        if on == 1:
            typing_Ani(f'적이 공격했지만 방어했다. {enemy_attack - block} 데미지를 입었다.', 0.05)
            hp -= (enemy_attack - block)
            on = 0
        else:
            answer = input('피할 곳을 선택하세요 (1 ~ 3) :')
            if answer == run:
                typing_Ani('공격을 회피했다!', 0.05)
            else:
                typing_Ani(f'적이 공격했다. {enemy_attack} 데미지를 입었다.', 0.05)
                hp -= enemy_attack
    if hp <= 0:
        typing_Ani('사망', 0.05)
    elif enemy_hp <= 0:
        typing_Ani('승리했다.', 0.05)
    
    


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
    typing_Ani('로봇기술자 : 나는 이곳에서 탈출하려는 로봇쟁이다.', 0.05)
    typing_Ani('야바위꾼 심해어  : 닝겐주제에 여기서 어떻게 탈출한다는 거지?', 0.05)
    typing_Ani('로봇기술자 : crystal을 모으면 탈출할 수 있어.', 0.05)
    typing_Ani('(크리스탈을 보여준다.)', 0.05)
    typing_Ani('야바위꾼 심해어  : 오 마침 나한테 그게 있는데.', 0.05)
    typing_Ani('야바위꾼 심해어: 나랑 야바위을 해서 이기면 이걸 주지. 기회는 3번', 0.05)
    typing_Ani('로봇기술자 : ㅇㅇ 뜨자', 0.05)
    typing_Ani('규칙: 1 ~ 5 중 하나를 고르세요', 0.05)
    typing_Ani('하지만 그 중 1개만 이길 수 있는 카드입니다.', 0.05)
    num = 0
    real = random.randint(1, 5)
    for i in range(3):
        num = input('숫자 입력 :')
        if num == real:
            typing_Ani('성공! you win!', 0.05)
            crystal + 1
            break
        else:
            typing_Ani('실패! try again!', 0.05)
    
    return crystal
def read_it():
    crystal = 0
    ok = 0
    typing_Ani('돌판 : [여기에 있는 주문을 거꾸로 외워라.]', 0.05)
    typing_Ani('돌판 : [그러면 하나를 얻을 것이니라.]', 0.05)
    typing_Ani('로봇기술자 : 주문외우기 정도면 날먹이지.', 0.05)
    typing_Ani('로봇기술자 : 이 글자가 주문인것 같은데 읽어볼까?')
    typing_Ani('규칙 : 제시된 텍스트를 거꾸로 입력하세요.', 0.05)
    list = ['when_you_collect_all_4_crystals', 'the_door_to_the_boss_room_will_open.',
             'if_you_defeat_that_evil_monster', 'you_will_be_able_to_escape_from_here']
    unlist = []
    for i in list:
        unlist.append(i[::-1])
    for i in unlist:
        print(i)    
        answer = input('주문 입력 : ')
        while ok == 4:
            if answer == list[i]:
                typing_Ani('땅이 움직인다!', 0.05)
                ok += 1
            else:
                typing_Ani('주문이 틀린 것 같아.', 0.05)
        typing_Ani('땅이 열리고 크리스탈이 나타났다!', 0.05)
        crystal += 1

    return crystal
def password():
    crystal = 0
    no = 0
    yes = 0
    typing_Ani('로봇기술자 : 이 상자는 뭐지?', 0.05)
    typing_Ani('(아래 돌 버튼이 있다.)', 0.05)
    typing_Ani('로봇기술자 : 버튼을 눌러볼까?', 0.05)
    typing_Ani('규칙 : 1자리 비밀번호를 3번 연속 맞추세요. 기회 10번', 0.05)
    random_password = random.randint(0, 9)  
    while yes < 3:
        if no != 10:
            if random_password == int(input('비밀번호 입력 : ')):
                yes += 1
                typing_Ani('비밀번호 일치', 0.05)
                random_password = random.randint(0, 9)  
            else:
                no += 1
                typing_Ani('비밀번호 불일치', 0.05)
        else:
            typing_Ani('비밀번호가 리셋됩니다.', 0.05)
            yes = 0
            no = 0
            random_password = random.randint(0, 9)  
    typing_Ani('성공! 상자가 열렸습니다.', 0.05)
    crystal += 1
    return crystal
            

def story():

    #1.처음
    typing_Ani("로봇기술자 : 난 이게임의 주인공이다.", 0.05)
    typing_Ani("로봇기술자 : 희귀한 광물을 얻으러 출장을 나왔다.", 0.05)
    typing_Ani("로봇기술자 : 이번에 나는 한 심해동굴을 탐사할거다.", 0.05)
    typing_Ani("로봇기술자 : 이 동굴은 들어가면 다시 못나온다고 했다.", 0.05)
    typing_Ani("로봇기술자 : 하지만 난 그 말을 무시하고 그대로 들어갔다", 0.05)
    typing_Ani("로봇기술자 : 이번 일도 실패하면 난 해고되기 때문이다.", 0.05)
    typing_Ani("로봇기술자 : 해고되면 우리 가족은 뭘 먹고 살라느-", 0.05)
    typing_Ani("(잠수함 충돌)", 0.05)
    typing_Ani("[당신은 심해동굴에서 탈출해야 합니다.]", 0.05)
    typing_Ani("[4]개의 크리스탈을 모으면 당신을 [탈출] 시켜드리겠습니다.", 0.05)
    typing_Ani("회썰러나간 로봇쟁이 시작")


def ending():
    typing_Ani('로봇기술자 : 드디어 탈출이다!!!', 0.05)
    typing_Ani('크라켄 : (사망)', 0.05)
    typing_Ani('로봇기술자 : 이제 가서 뭐하지?', 0.05)
    typing_Ani('로봇기술자 : 아 맞다. 여기 크리스탈이랑 크라캔이 있었지!', 0.05)
    typing_Ani('로봇기술자 : 이걸 팔아서 큰1돈을 벌거야!', 0.05)
    typing_Ani('그 뒤 로봇쟁이는 타코야끼를 팔아서 부1자가 되었다고한다.', 0.05)
    typing_Ani('회썰러나간 로봇쟁이 -the end-', 0.05)
    typing_Ani('개발 : 곽주찬')
    typing_Ani('tanks for playing', 0.05)