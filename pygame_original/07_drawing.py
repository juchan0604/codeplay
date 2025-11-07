# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()#초기화 (반드시 필요)

#화면크기 설정
screen_width = 800 #가로크기
screen_height = 800 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("그려그려그림판")

#FPS
clock = pygame.time.Clock()

r = 120
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수

    #2 이벤트 처리(키보드, 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

    # 배경색 설정
    screen.fill((150, 125, 100))

    # 직선 그리기 
                #   어따그려?, 무슨색?(3), 시작어디?(2), 끝어디?(2), 굵기는?
    #pygame.draw.line(1, 2, 3, 4, 5)  
    # pygame.draw.line(screen, (0, 55, 0), (0, 0) , (screen_width, screen_height), 50) # 대상, 색상, 시작점, 끝점, 굵기)
    # pygame.draw.line(screen, (0, 0, 0), (0, screen_height), (screen_width, 0), 50)

    # measure = screen_width / 10

    # for i in range(10):
    #     pygame.draw.line(screen, (0, 0, 0), (0, i*measure), (screen_width, i*measure), 2) # 가로줄
    #     pygame.draw.line(screen, (0, 0, 0), (i*measure, 0), (i*measure, screen_height), 2) # 세로줄
    ll = 760 // 18
    offset = 22
    # 선 여러개 긋기 (반복문 활용)
    for i in range(0, 800, ll): # 세로줄
        pygame.draw.line(screen, (0, 0, 0), (i + offset, 0), (i + offset, screen_width))
    for i in range(0, 800, ll): # 가로줄
        pygame.draw.line(screen, (0, 0, 0), (0, i + offset), (screen_width, i + offset))
    pygame.draw.line(screen, (0, 0, 0), (0, screen_height), (screen_width, screen_height), offset * 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, screen_height), offset * 2)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (screen_width, 0), offset * 2)
    pygame.draw.line(screen, (0, 0, 0), (screen_width, 0), (screen_width, screen_height), offset * 2)
    #원 그리기
    
    start_point = (ll * 3) + offset
    for k in range(3):    
        for i in range(3):
            pygame.draw.circle(screen, (0, 0, 0), (start_point + (k * (6 * ll)), start_point + (i * (6 * ll))), ll / 8)
    
    
    pygame.display.update() #게임화면을 새로고침해줌.

# 종료시간 살짝 늦추기
# pygame.time.delay(2000)
#종료처리
pygame.quit()

