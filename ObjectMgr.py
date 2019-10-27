from pico2d import *

# Object List
ObjLst = []

# Object
Player = []
PlayerBullet = []
Monster = []
MonsterBullet = []
Item = []

ObjLst.append(Player)
ObjLst.append(PlayerBullet)
ObjLst.append(Monster)
ObjLst.append(Item)

Event = 0


def Update():
    global Event
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            Event = GameObj.Update()

            if Event == -1:
                del GameObj
                ObjLst.pop()

    pass


def Render():
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            GameObj.Render()

    pass
