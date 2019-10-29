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
    image_HpBar = None

    def __init__(self, PosX, PosY, ScaleX, ScaleY, Hp, Speed, Radius, Exp, FileName):
        if CMonster.image[0] is None:
            CMonster.image[0] = load_image("Resource/Monster/Enemy01.png")

        if CMonster.image[1] is None:
            CMonster.image[1] = load_image("Resource/Monster/Enemy02.png")

        if CMonster.image[2] is None:
            CMonster.image[2] = load_image("Resource/Monster/Enemy03.png")

        if CMonster.image_HpBar is None:
            CMonster.image_HpBar = load_image("Resource/UI/MonsterHpBar_2.png")

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

        # HpBar 변수.
        self.hpRadio = 0.0
        self.originCX = 70
        self.hpCX = 70.0
        self.hpCY = 11
        self.hpPosX = self.x

        pass

    def Handle_Events(self):
        pass

    def Update(self):
        global Lst_CoinLottery

        if self.IsDead:
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
            self.hp = 0
            self.IsDead = True

        # Hp Ratio
        self.hpRadio = self.hp / self.max_hp
        self.hpCX = self.originCX * self.hpRadio
        self.hpPosX = self.x - (self.originCX - self.hpCX) / 2

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
            CMonster.image_HpBar.clip_draw(0, 0, int(self.hpCX), self.hpCY, self.hpPosX, self.y - 50)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass

    pass
