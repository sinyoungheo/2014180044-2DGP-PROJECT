from pico2d import *
import random
import GameFramework

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class CBossStage1:
    def __init__(self):
        self.IsDead = False
        self.frame = 0
        self.x, self.y = 360, 960
        self.scaleX, self.scaleY = 300, 256
        self.speed = 400
        self.radius = 128
        self.hp = 5000
        self.max_hp = self.hp
        self.exp = 1000

        self.image = load_image("Resource/Monster/Boss01.png")
        self.image_HpBarEmpty = load_image("Resource/UI/MonsterHpBarEmpty.png")
        self.image_HpBar = load_image("Resource/UI/MonsterHpBar.png")

        # HpBar 변수.
        self.hpRadio = 0.0
        self.originCX = 118
        self.hpCX = 118.0
        self.hpCY = 19
        self.hpPosX = self.x

        pass

    def Handle_Events(self):
        pass

    def Update(self):
        # Animation
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * GameFramework.frame_time) % 4

        # Move
        if self.x > 700:
            self.x -= self.speed * GameFramework.frame_time

        # Hp Ratio
        self.hpRadio = self.hp / self.max_hp
        self.hpCX = self.originCX * self.hpRadio
        self.hpPosX = self.x - (self.originCX - self.hpCX) / 2

        pass

    def Render(self):
        if not self.IsDead:
            self.image.clip_draw(int(self.frame) * 76, 0, 76, 51, self.x, self.y, self.scaleX, self.scaleY)

            self.image_HpBarEmpty.clip_draw(0, 0, 119, 16, self.x, self.y - 50)
            self.image_HpBar.clip_draw(0, 0, int(self.hpCX), self.hpCY, self.hpPosX, self.y - 50)
        pass

    ######################################


    pass