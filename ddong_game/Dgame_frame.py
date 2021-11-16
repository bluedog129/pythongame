import pygame
import random
#########################################################

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 길이
screen_height = 640 # 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("ddong game")

# 캐릭터의 위치
character = pygame.image.load("C:/Users/blued/git/PythonGames/ddong_game/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height
# 똥의 위치
enemy = pygame.image.load("C:/Users/blued/git/PythonGames/ddong_game/ddong.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0,screen_width-enemy_width)
enemy_y_pos = 0

# 이동할 좌표
character_to_x = 0
character_to_y = 0

# 이동 속도
character_speed = 0.5
enemy_speed = 0.3

# FPS
clock = pygame.time.Clock()
##################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/blued/git/PythonGames/ddong_game/background.png")


running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_UP:
                character_to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                character_to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0
    
    

    # 3. 게임 캐릭터 위치 정의
    
    # 캐릭터 위치 정의
    character_x_pos += character_to_x * dt
    character_y_pos += character_to_y * dt
    # 캐릭터 이동 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 캐릭터 이동 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 똥 캐릭터 위치 이동
    # 충돌이 일어나기 전까지 떨어짐 반복
    enemy_y_pos += enemy_speed * dt
    if enemy_y_pos > screen_height - enemy_height: # enemy_y_pos < screen_height-enemy_height 일때까지 떨어짐
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0,screen_width-enemy_width)
    
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요!")
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경화면 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초정도 대기 (ms)

# pygame 종료
pygame.quit()