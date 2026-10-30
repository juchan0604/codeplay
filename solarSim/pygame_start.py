# -*- coding: utf-8 -*-
import pygame
import random
pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption('코딩쌤 초초초초초초초초초초초초초초초초초초초')

#이미지 불러오기(저장)
bg =pygame.image.load("solarSim/src/minecraft.jpg") # Relative Path

#이벤트 루프 - 종료까지 대기
running = True # 실행중인지 확인

while running: #반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #                red                  green                  blue
    screen.blit(bg, (0, 0)) # blit = 배경 그리기
    #screen.fill((random.randint(0,254), random.randint(0,254), random.randint(0,254))) #  배경을 이미지가 아닌 색으로 지정하기
    pygame.display.update() # 게임화면을 새로고침해줌.


#종료처리
pygame.quit()