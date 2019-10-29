from pico2d import *
import random
import Item
import ObjectMgr

# # Random Item 생성.
# Lst_CoinLottery = []
# for n in range(0, 50):
#     Lst_CoinLottery.append(0)
# for n in range(0, 30):
#     Lst_CoinLottery.append(1)
# for n in range(0, 20):
#     Lst_CoinLottery.append(2)
# for n in range(0, 10):
#     Lst_CoinLottery.append(3)
#
# random.shuffle(Lst_CoinLottery)


class CMonster:
    image = [None, None, None]

    def __init__(self, PosX, PosY, ScaleX, ScaleY, Hp, Speed, Radius, Exp, FileName):
        if CMonster.image[0] is None:
            CMonster.image[0] = load_image("Resource/Monster/Enemy01.png")

        if CMonster.image[1] is None:
            CMonster.image[1] = load_image("Resource/Monster/Enemy02.png")

        if CMonster.image[2] is None:
            CMonster.image[2] = load_image("Resource/Monster/Enemy03.png")

        self.IsDead = False
        self.frame = random.randint(0, 3)
        self.x, self.y = PosX, PosY
        self.scaleX, self.scaleY = ScaleX, ScaleY
        self.speed = Speed
        self.radius = Radius
        self.hp = Hp
        self.max_hp = self.hp
        self.exp = Exp
        self.filename = FileName

    def Handle_Events(self):
        pass

    def Update(self):
        global Lst_CoinLottery

        if self.IsDead:
            # # Item 생성.
            # coin_num = random.choice(Lst_CoinLottery)
            # FileName = ""
            # if coin_num == 0:
            #     FileName = "item_coin0.png"
            #
            # # PosX, PosY, CX, CY, Radius, ScaleX, ScaleY, Target, FileName
            # GameObject = Item.CItem(self.x, self.y, 64, 64, 16, 64, 64, None, FileName)
            # ObjectMgr.Add_GameObject(GameObject, "Item")
            return -1

        # Animation
        self.frame = (self.frame + 1) % 4

        # Move
        self.y = self.y - self.speed

        # OffSet
        if self.y <= 0:
            self.IsDead = True
            pass

        # Check Hp
        if self.hp <= 0:
            self.IsDead = True

        return 0
        pass

    def Render(self):
        index = 0

        if self.filename == "Enemy01.png":
            index = 0
        elif self.filename == "Enemy02.png":
            index = 1
        elif self.filename == "Enemy03.png":
            index = 2

        if not self.IsDead:
            CMonster.image[index].clip_draw(self.frame * 76, 0, 76, 51, self.x, self.y, self.scaleX, self.scaleY)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass

    pass
