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

# 배경색 설정

screen.fill((255, 255, 255))

r = 120
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수

    #2 이벤트 처리(키보드, 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False
    #건
    for i in range(3):
        pygame.draw.line(screen, (0, 0, 0), (50 + 15 * i , 150 + 15 * i), (150 + 15 * i, 50 + 15 * i), 20)
    #곤
    for i in range(3):
        pygame.draw.line(screen, (0, 0, 0), (600 + 15 * i , 700 + 15 * i), (700 + 15 * i, 600 + 15 * i), 20)
        pygame.draw.line(screen, (255, 255, 255), (600, 600), (700, 700), 15)
    #감
    for i in range(3):
        pygame.draw.line(screen, (0, 0, 0), (700 + 15 * i, 175 - 15 * i), (600 + 15 * i, 75 - 15 * i), 20)
    for i in range(2):
        pygame.draw.line(screen, (255, 255, 255), (700, 120), (705, 80), 15)
    #태극
    for i in range(5):  
        pygame.draw.circle(screen, (225, 0, 225), (400, 400), 150)
    
    
    pygame.display.update() #게임화면을 새로고침해줌.



#종료처리
pygame.quit()