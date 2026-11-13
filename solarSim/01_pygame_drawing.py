# -*- coding: utf-8 -*-
import pygame
import random
pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption('코딩쌤 초초초초초초초초초초초초초초초초초초초')

#이벤트 루프 - 종료까지 대기
running = True # 실행중인지 확인

r = 120
while running: # 반복
    # 2 이벤트 처리(키보드 마우스 등 화면조작 관련)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경색 설정
    screen.fill((255, 255, 255)) # 튜플

    # 직선 그리기 
    pygame.draw.line(screen, (25, 225, 125), (0, 0), (screen_width, screen_height), 30) # (대상, 색상, 시작점, 끝점, 굵기)
    pygame.draw.line(screen, (0, 255, 0), (0, screen_height), (screen_width, 0), 30)

    # 선 여러개 긋기 (반복문 활용)
    for i in range(0, 480, 30): # 세로줄
        pygame.draw.line(screen, (0, 0, 225), (i, 0), (i, 640))
    for i in range(0, 640, 30): # 가로줄
        pygame.draw.line(screen, (0, 0, 225), (0, i), (480, i))

    # 원 그리기
    pygame.draw.circle(screen, (0, 255, 100), (screen_width / 2, screen_height / 2), 100) # 채워진 원 (대상, 색상, 중심점, 반지름)
    pygame.draw.circle(screen, (255, 0, 0), (screen_width / 2, screen_height / 2), 200, 50) # 테두리 원 (대상, 색상, 중심점, 반지름, 선굵기)

    # 사각형
    pygame.draw.rect(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 100)) # 채워진 사각형 (대상, 색상, 시작점 + 가로크기 + 세로크기)
    pygame.draw.rect(screen, (155, 155, 55), (screen_width / 2, screen_height / 2, 100, 200), 5) # 테두리 사각형 (대상, 색상, 시작점 + 가로크기 + 세로크기, 선 굵기)

    # 타원
    pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 200)) # 채워진 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기)
    pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2, screen_height / 2, 200, 100), 5) # 테두리 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기, 선 굵기)

    pygame.draw.ellipse(screen, (55, 55, 255), (screen_width / 2 - 100, screen_height / 2 - 100, 100, 100)) # 채워진 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기)
    pygame.draw.ellipse(screen, (155, 155, 55), (screen_width / 2 - 100, screen_height / 2 - 100, 100, 100), 5) # 태두리 타원 (대상, 색상, 시작점 + 가로크기 + 세로크기, 선 굵기)

    # 다각형
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 0], [0, 200], [200, 200]]) # 삼각형 / 점은 3개 이상. 위쪽부터 반시계방향으로 좌표 작성
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100]]) # 육각형. 점의 개수만큼 추가하면 됨.

    # 화면에 그리기
    pygame.display.update() # 게임 화면을 새로고침해줌.

#종료처리
pygame.quit()