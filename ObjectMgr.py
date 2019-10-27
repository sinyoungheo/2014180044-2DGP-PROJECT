from pico2d import *
import Player

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
ObjLst.append(MonsterBullet)
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



def Add_GameObject(GameObject, ObjID):
    if ObjID == "Player":
        pass

    if ObjID == "PlayerBullet":
        pass

    if ObjID == "Monster":
        pass

    if ObjID == "MonsterBullet":
        pass

    if ObjID == "Item":
        pass