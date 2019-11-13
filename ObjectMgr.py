import CollisionMgr

# Object List
ObjLst = []

# Object
LstPlayerLaser = []
LstPlayer = []
LstPlayerPet = []
LstPlayerBullet = []
LstMonster = []
LstMonsterBullet = []
LstItem = []
LstEffect = []
LstUI = []

ObjLst.append(LstPlayerLaser)
ObjLst.append(LstPlayer)
ObjLst.append(LstPlayerPet)
ObjLst.append(LstPlayerBullet)
ObjLst.append(LstMonster)
ObjLst.append(LstMonsterBullet)
ObjLst.append(LstItem)
ObjLst.append(LstEffect)
ObjLst.append(LstUI)

Event = 0


# KeyInput Event
def Handle_Events():
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            GameObj.Handle_Events()

    pass


# GameObject Update
def Update():
    global Event
    global ObjLst

    for List in ObjLst:
        # num = len(List)
        # print(num)
        for GameObj in List:
            Event = GameObj.Update()

            # 게임 오브젝트 사망시 제거.
            if Event == -1:
                List.remove(GameObj)
                del GameObj

    # CollisionMgr
    global LstPlayer
    global LstMonster
    global LstPlayerBullet
    global LstItem

    CollisionMgr.Collision_Monster_PLBullet(LstMonster, LstPlayerBullet, LstPlayer[0])
    CollisionMgr.Collision_Player_Item(LstPlayer, LstItem)

    pass


# GameObject Render
def Render():
    global ObjLst

    for List in ObjLst:
        for GameObj in List:
            GameObj.Render()

    pass


# GameObject Add
def Add_GameObject(GameObject, ObjID):
    global LstPlayer
    global LstPlayerPet
    global LstPlayerBullet
    global LstMonster
    global LstMonsterBullet
    global LstItem
    global LstEffect
    global LstUI

    if ObjID == "Player":
        LstPlayer.append(GameObject)
        pass

    if ObjID == "PlayerPet":
        LstPlayerPet.append(GameObject)

    if ObjID == "PlayerBullet":
        LstPlayerBullet.append(GameObject)
        pass

    if ObjID == "PlayerLaser":
        LstPlayerLaser.append(GameObject)
        pass

    if ObjID == "Monster":
        LstMonster.append(GameObject)
        pass

    if ObjID == "MonsterBullet":
        LstMonsterBullet.append(GameObject)
        pass

    if ObjID == "Item":
        LstItem.append(GameObject)
        pass

    if ObjID == "Effect":
        LstEffect.append(GameObject)

    if ObjID == "UI":
        LstUI.append(GameObject)
