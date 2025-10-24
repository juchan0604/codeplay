# -*- coding: utf-8 -*-
import pygame
pygame.init()#초기화 (반드시 필요)

#화면크기 설정
screen_width = 500 #가로크기
screen_height = 500 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("똥피하기-코드플레이")

#FPS
clock = pygame.time.Clock()

#이동속도 고정해주기
character_speed = 0.1

#이미지 불러오기
bg = pygame.image.load("pygame_original/source/Iseeyou.png")#상대경로로 불러와야 다른 컴에서도 적용

#스프라이트 불러오기
character = pygame.image.load("pygame_original/source/gd.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height / 2) - (character_height / 2)
#이동할 값
to_x = 0
to_y = 0

#이벤트 루프 - 종료까지 대기
running = True #실행중인지 확인
while running:
    dt = clock.tick(30) #게임화면이 초당 리프레시되는 횟수

    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
        if event.type == pygame.KEYDOWN: #키보드 눌림 확인
            if event.key == pygame.K_a: #왼쪽 화살표
                to_x -= 1
            elif event.key == pygame.K_d: #오른쪽 화살표
                to_x += 1
            elif event.key == pygame.K_w: #위쪽 화살표
                to_y -= 1
            elif event.key == pygame.K_s: #아래쪽 화살표 K_UP/K_DOWN?K_LEFT/K_RIGHT
                to_y += 1
        if event.type == pygame.KEYUP: # 키보드에서 손을 뗐을 떄 중지
            if event.key == pygame.K_a or event.key == pygame.K_d: #가로움직임
                to_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s: #세로움직임
                to_y = 0

    #추가한 이미지들을 화면에 띄우기
    character_xPos += to_x * dt #스프라이트에 위치 반영
    character_yPos += to_y * dt #스프라이트에 위치 반영
    
    # 가로 스크린내 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    
    # 세로 스크린내 안벗어나게
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height
    
    screen.blit(bg, (0, 0))#blit = 배경 그리기
    screen.blit(character, (character_xPos, character_yPos))
    
    pygame.display.update()# 게임화면을 새로고침해줌.

#종료처리
pygame.quit()