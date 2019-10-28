from pico2d import *
import random
import ObjectMgr
import Player
import Monster


# 배경 이미지
image = None

# Monster01 생성 시간
time_CreateMonster = 10.0
time_UpdateCreateMonster = 10.0

Pos_CreateX = 52
Pos_CreateY = 960
Pos_OffsetX = 114


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
    # Object Update
    ObjectMgr.Update()

    # Monster 생성.
    global time_CreateMonster
    global time_UpdateCreateMonster
    global Pos_CreateX
    global Pos_CreateY
    global Pos_OffsetX

    # Monster 01 생성.
    time_CreateMonster = time_CreateMonster + 0.1

    if time_CreateMonster >= time_UpdateCreateMonster:
        for n in range(random.randint(0, 2 + 1), random.randint(3, 5 + 1)):
            PosX = Pos_CreateX + Pos_OffsetX * n
            # x, y, scaleX, scaleY, hp, speed, radius, exp, filename
            GameObject = Monster.CMonster(PosX, Pos_CreateY, 114, 76, 100, 3, 25, 100, "Enemy01.png")

            ObjectMgr.Add_GameObject(GameObject, "Monster")
            pass

        Pos_CreateX = 76
        time_CreateMonster = 0.0

    # Monster 02 생성

    # Monster 03 생성

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
