import ObjectMgr
import math
import Effect
import Item
import random

# Random Item 생성.
Lst_CoinLottery = []
for n in range(0, 40):
    Lst_CoinLottery.append(0)
for n in range(0, 25):
    Lst_CoinLottery.append(1)
for n in range(0, 20):
    Lst_CoinLottery.append(2)
for n in range(0, 15):
    Lst_CoinLottery.append(3)

random.shuffle(Lst_CoinLottery)

Lst_ItemLottery = []
for n in range(0, 70):
    Lst_ItemLottery.append(0)   # 꽝
for n in range(0, 15):
    Lst_ItemLottery.append(1)   # dual shot
for n in range(0, 15):
    Lst_ItemLottery.append(2)   # egg
for n in range(0, 15):
    Lst_ItemLottery.append(3)   # formation
for n in range(0, 15):
    Lst_ItemLottery.append(4)   # invincible
for n in range(0, 15):
    Lst_ItemLottery.append(5)   # magnet

random.shuffle(Lst_ItemLottery)


# 원 충돌 검사.
def Check_Collision(Dst, Src):
    Distance = math.sqrt(pow(Dst.x - Src.x, 2) + pow(Dst.y - Src.y, 2))
    Sum_Radius = Dst.radius + Src.radius

    if Distance <= Sum_Radius:
        return True
    else:
        return False
    pass


# Monster & Player 충돌.
def Collision_Monster_Player(DstLst, SrcLst):
    # DstLst - Monster
    # SrcLst - Player
    pass


# Monster & Player Bullet 충돌.
def Collision_Monster_PLBullet(DstLst, SrcLst, Player):
    # DstLst - Monster
    # SrcLst - Player Bullet
    global Lst_CoinLottery

    for Dst in DstLst:
        for Src in SrcLst:
            if Check_Collision(Dst, Src):
                # Delete Bullet
                Src.DeadObject()

                # Monster Hp 감소
                Dst.hp -= Src.damage
                # Monster 사망 시 Player Exp 증가.
                if Dst.hp <= 0:
                    Dst.IsDead = True
                    Player.exp += Dst.exp

                    # Monster 사망 Effect
                    # PosX, PosY, CX, CY, Speed, IsSingleEffect, IsAnimationEndDead, MaxFrame, LifeTime, ScaleX, ScaleY, FileName
                    GameObj = Effect.CEffect(Dst.x, Dst.y, 76, 51, 0.3, False, False, 4, 2.4, 114, 76, "dust.png")
                    ObjectMgr.Add_GameObject(GameObj, "Effect")

                    # Item - Coin 생성.
                    coin_num = random.choice(Lst_CoinLottery)
                    FileName = ""
                    if coin_num == 0:
                        FileName = "item_coin0.png"
                    elif coin_num == 1:
                        FileName = "item_coin1.png"
                    elif coin_num == 2:
                        FileName = "item_coin2.png"
                    elif coin_num == 3:
                        FileName = "item_coin3.png"

                    # PosX, PosY, CX, CY, Radius, ScaleX, ScaleY, Target, FileName
                    GameObject = Item.CItem(Dst.x, Dst.y, 64, 64, 16, 64, 64, Player, FileName)
                    ObjectMgr.Add_GameObject(GameObject, "Item")

                    # Item 생성
                    item_num = random.choice(Lst_ItemLottery)
                    ItemFileName = ""
                    if item_num != 0:
                        if item_num == 1:
                            ItemFileName = "item_dualshot.png"
                        elif item_num == 2:
                            ItemFileName = "item_egg.png"
                        elif item_num == 3:
                            ItemFileName = "item_formation.png"

                        pass
                pass

    return False
    pass


# Player & Item 충돌.
def Collision_Player_Item(DstLst, SrcLst):
    # DstLst - Player
    # SrcLst - Item

    for Dst in DstLst:
        for Src in SrcLst:
            if Check_Collision(Dst, Src):
                # Item 제거.
                Src.IsDead = True
                # Item == Coin01
                if Src.filename == "item_coin0.png":
                    Dst.coin_cnt += 1
                if Src.filename == "item_coin1.png":
                    Dst.coin_cnt += 10
                if Src.filename == "item_coin2.png":
                    Dst.coin_cnt += 50
                if Src.filename == "item_coin3.png":
                    Dst.coin_cnt += 100

                pass
    pass
