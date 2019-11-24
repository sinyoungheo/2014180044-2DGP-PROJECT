from pico2d import *
import GameFramework
import random
import ObjectMgr
import Player
import Monster
import Boss_Stage1

# 배경 이미지
image = None

# 맵 스크롤링
scroll_y = 4
first_image_y = 1440
second_image_y = 480

# Monster01 생성 시간
time_CreateMonster01 = 10.0
time_UpdateCreateMonster01 = 10.0

# Monster02 생성 시간
time_CreateMonster02 = 7.5
time_UpdateCreateMonster02 = 15.0

# Monster03 생성 시간
time_CreateMonster03 = 9.0
time_UpdateCreateMonster03 = 9.0

# Monster 생성 위치.
Pos_CreateX = 52
Pos_CreateY = 960
Pos_OffsetX = 114

# Monster 생성 인자.
Monster_Hp = 100
Monster_Speed = 3
Monster_Exp = 50

# Stage1 Boss 생성.
IsCreateBoss_Stage1 = False
BossCreateTime_Stage1 = 3.0

# Game Play Time
PlayTime = 0.0


def Enter():
    # 배경 이미지
    global image
    image = load_image("Resource/Scene/Scene_01.png")

    # Player 생성
    GameObject = Player.CPlayer()
    ObjectMgr.Add_GameObject(GameObject, "Player")


def Exit():
    global image
    del image
    image = None

    # ObjectMgr.All_Delete_GameObject()

    global PlayTime
    global time_CreateMonster01
    global time_CreateMonster02
    global time_CreateMonster03
    global IsCreateBoss_Stage1
    global BossCreateTime_Stage1

    PlayTime = 0.0
    time_CreateMonster01 = 0.0
    time_CreateMonster02 = 0.0
    time_CreateMonster03 = 0.0

    IsCreateBoss_Stage1 = False
    BossCreateTime_Stage1 = 0.0
    pass


def Handle_Events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.Quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.Quit()

    ObjectMgr.Handle_Events()
    pass


def Update():
    global scroll_y
    global first_image_y
    global second_image_y

    first_image_y -= scroll_y
    second_image_y -= scroll_y

    if first_image_y <= -480:
        first_image_y = 1440

    if second_image_y <= -480:
        second_image_y = 1440

    # Game Play Time
    global PlayTime
    PlayTime = get_time()

    # print(PlayTime)

    # Object Update
    ObjectMgr.Update()

    # Monster 생성.
    global time_CreateMonster01
    global time_CreateMonster02
    global time_CreateMonster03
    global time_UpdateCreateMonster01
    global time_UpdateCreateMonster02
    global time_UpdateCreateMonster03

    global Pos_CreateX
    global Pos_CreateY
    global Pos_OffsetX
    global Monster_Hp
    global Monster_Speed
    global Monster_Exp

    # Monster 01 생성.
    time_CreateMonster01 += 0.1

    if time_CreateMonster01 >= time_UpdateCreateMonster01:
        for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
            PosX = Pos_CreateX + Pos_OffsetX * n
            Monster_Hp = 100
            Monster_Speed = 400
            Monster_Exp = 50
            # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
            GameObject = Monster.CMonster(PosX, Pos_CreateY, 114, 76, Monster_Hp, Monster_Speed, 25, Monster_Exp,
                                          "Enemy01.png")

            ObjectMgr.Add_GameObject(GameObject, "Monster")
            pass

        Pos_CreateX = 76
        time_CreateMonster01 = 0.0

    # Monster 02 생성
    Pos_CreateX = 76
    if PlayTime >= 20.0:
        time_CreateMonster02 += 0.1

        if time_CreateMonster02 >= time_UpdateCreateMonster02:
            for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
                PosX = Pos_CreateX + Pos_OffsetX * n
                Monster_Hp = 250
                Monster_Speed = 600
                Monster_Exp = 150
                # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
                GameObject = Monster.CMonster(PosX, Pos_CreateY, 114, 76, Monster_Hp, Monster_Speed, 25, Monster_Exp,
                                              "Enemy02.png")

                ObjectMgr.Add_GameObject(GameObject, "Monster")
                pass

            Pos_CreateX = 76
            time_CreateMonster02 = 0.0
        pass

    # Monster 03 생성
    Pos_CreateX = 76
    if PlayTime >= 30.0:
        time_CreateMonster03 += 0.1

        if time_CreateMonster03 >= time_UpdateCreateMonster03:
            for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
                PosX = Pos_CreateX + Pos_OffsetX * n
                Monster_Hp = 500
                Monster_Speed = 700
                Monster_Exp = 300
                # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
                GameObject = Monster.CMonster(PosX, Pos_CreateY, 114, 76, Monster_Hp, Monster_Speed, 25, Monster_Exp,
                                              "Enemy03.png")

                ObjectMgr.Add_GameObject(GameObject, "Monster")
                pass

            Pos_CreateX = 76
            time_CreateMonster03 = 0.0
        pass

    # Boss Monster 생성.
    global IsCreateBoss_Stage1
    global BossCreateTime_Stage1

    if PlayTime >= BossCreateTime_Stage1:
        if not IsCreateBoss_Stage1:
            # Stage1 보스 생성.
            ObjectMgr.Add_GameObject(Boss_Stage1.CBossStage1(ObjectMgr.LstPlayer[0]), "Monster")
            IsCreateBoss_Stage1 = True
            pass

    pass


def Render():
    global scroll_y
    global first_image_y
    global second_image_y

    # Object Render
    clear_canvas()

    # left, bottom, right, top, posX, posY, scaleX, scaleY
    image.clip_draw(0, 0, 384, 512, 360, first_image_y, 720, 960)

    # left, bottom, right, top, posX, posY, scaleX, scaleY
    image.clip_draw(0, 0, 384, 512, 360, second_image_y, 720, 960)

    # image.draw(360, 480, 720, 960)
    ObjectMgr.Render()

    update_canvas()
    # delay(0.015)
    pass


def Pause():
    pass


def Resume():
    pass
