from pico2d import *
import ObjectMgr
import Player

image = None


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
    ObjectMgr.Update()
    pass


def Render():
    clear_canvas()

    image.draw(360, 480, 720, 960)
    ObjectMgr.Render()

    update_canvas()
    pass


def Pause():
    pass


def Resume():
    pass
