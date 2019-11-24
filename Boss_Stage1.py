from pico2d import *
import random
import GameFramework
import ObjectMgr
import MathMgr
import MonsterBullet

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

time_CreateBullet = 0.0
time_UpdateCreateBullet = 0.2


class CBossStage1:
    def __init__(self, Target=None):
        self.IsDead = False
        self.frame = 0
        self.x, self.y = 360, 960
        self.scaleX, self.scaleY = 300, 256
        self.speed = 400
        self.radius = 128
        self.hp = 50000
        self.max_hp = self.hp
        self.exp = 1000

        if Target is not None:
            self.target = Target
        else:
            self.target = None

        self.image = load_image("Resource/Monster/Boss01.png")
        self.image_HpBarEmpty = load_image("Resource/UI/MonsterHpBarEmpty_0.png")
        self.image_HpBar = load_image("Resource/UI/MonsterHpBar_0.png")

        # HpBar 변수.
        self.hpRadio = 0.0
        self.originCX = 116
        self.hpCX = 116.0
        self.hpCY = 12
        self.hpPosX = self.x

        pass

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Animation
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * GameFramework.frame_time) % 4

        # Move
        if self.y > 840:
            self.y -= self.speed * GameFramework.frame_time

        # Hp Ratio
        self.hpRadio = self.hp / self.max_hp
        self.hpCX = self.originCX * self.hpRadio
        self.hpPosX = self.x - (self.originCX - self.hpCX) / 2

        # Create Bullet
        self.CreateBullet()

        return 0
        pass

    def Render(self):
        if not self.IsDead:
            self.image.clip_draw(int(self.frame) * 300, 0, 300, 256, self.x, self.y, self.scaleX, self.scaleY)

            self.image_HpBarEmpty.clip_draw(0, 0, 116, 12, self.x, self.y - 140)
            self.image_HpBar.clip_draw(0, 0, int(self.hpCX), self.hpCY, self.hpPosX, self.y - 140)
        pass

    ######################################

    def CreateBullet(self):
        global time_CreateBullet
        global time_UpdateCreateBullet

        time_CreateBullet += GameFramework.frame_time

        if time_CreateBullet >= time_UpdateCreateBullet:
            angle = MathMgr.CalcDegree(self, self.target)

            angle += random.randint(-5, 5)

            ObjectMgr.Add_GameObject(MonsterBullet.CMonsterBullet(self.x, self.y - 50.0, 500, 26, angle, True, "BossBullet_1"),
                                     "MonsterBullet")
            time_CreateBullet = 0.0
            pass

        pass

    pass
