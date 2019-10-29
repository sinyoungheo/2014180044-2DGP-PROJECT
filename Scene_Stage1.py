from pico2d import *
import random
import ObjectMgr
import Player
import Monster

# 배경 이미지
image = None

# Monster01 생성 시간
time_CreateMonster01 = 10.0
time_UpdateCreateMonster01 = 10.0

# Monster 생성 위치.
Pos_CreateX = 52
Pos_CreateY = 960
Pos_OffsetX = 114

# Monster 생성 인자.
Monster_Hp = 100
Monster_Speed = 3
Monster_Exp = 50

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
    pass


def Handle_Events():
    ObjectMgr.Handle_Events()
    pass


def Update():
    # Game Play Time
    global PlayTime
    PlayTime = get_time()

    # Object Update
    ObjectMgr.Update()

    # Monster 생성.
    global time_CreateMonster01
    global time_UpdateCreateMonster01
    global Pos_CreateX
    global Pos_CreateY
    global Pos_OffsetX
    global Monster_Hp
    global Monster_Speed
    global Monster_Exp

    # Monster 01 생성.
    time_CreateMonster01 = time_CreateMonster01 + 0.1

    if time_CreateMonster01 >= time_UpdateCreateMonster01:
        for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
            PosX = Pos_CreateX + Pos_OffsetX * n
            Monster_Hp = 100
            Monster_Speed = 3
            Monster_Exp = 50
            # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
            GameObject = Monster.CMonster(PosX, Pos_CreateY, 114, 76, Monster_Hp, Monster_Speed, Monster_Exp, 100, "Enemy01.png")

            ObjectMgr.Add_GameObject(GameObject, "Monster")
            pass

        Pos_CreateX = 76
        time_CreateMonster = 0.0

    # Monster 02 생성
    if PlayTime >= 30.0:
        pass

    # Monster 03 생성
    if PlayTime >= 60.0:
        pass

    pass


def Render():
    # Object Render
    clear_canvas()

    image.draw(360, 480, 720, 960)
    ObjectMgr.Render()

    update_canvas()
    delay(0.015)
    pass


def Pause():
    pass


def Resume():
    pass
