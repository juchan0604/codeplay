# -*- coding: utf-8 -*-
import pygame
import math
pygame.init() # 초기화 (반드시 필요)

#화면크기 설정
screen = pygame.display.set_mode((1600, 700))

#화면 타이틀 (제목창)
pygame.display.set_caption('우주는 이제 재배맨이 지배한다!!!')

screen.fill((30, 30, 40))
# pygame.draw.rect(screen, (150, 150, 150), (200, 150, 150, 100))
# pygame.draw.rect(screen, (255, 165, 0), (500, 150, 150, 100))
# pygame.draw.rect(screen, (178, 255, 89), (800, 150, 150, 100))
# pygame.draw.rect(screen, (255, 140, 0), (1100, 150, 150, 100))
# pygame.draw.rect(screen, (210, 105, 30), (200, 400, 150, 100))
# pygame.draw.rect(screen, (210, 180, 140), (500, 400, 150, 100))
# pygame.draw.rect(screen, (0, 255, 255), (800, 400, 150, 100))
# pygame.draw.rect(screen, (0, 0, 255), (1100, 400, 150, 100))
pygame.draw.(screen, (255, 0, 0), (400, 190), 150)


# Windows 기본 한글 폰트 (맑은 고딕)
font = pygame.font.SysFont('malgungothic', 28)
small_font = pygame.font.SysFont('malgungothic', 20)

#이벤트 루프 - 종료까지 대기
running = True # 실행중인지 확인

while running: #반복
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update() # 게임화면을 새로고침해줌.


#종료처리
pygame.quit()