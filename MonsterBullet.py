from pico2d import *
import random
import GameFramework
import math
import MathMgr


class CMonsterBullet:
    image = [None, None, None]

    def __init__(self, PosX, PosY, Speed, Radius, Angle, IsSetDir, FileName):
        if CMonsterBullet.image[0] is None:
            CMonsterBullet.image[0] = load_image("Resource/Bullet/BossBullet_1.png")

        if CMonsterBullet.image[1] is None:
            CMonsterBullet.image[1] = load_image("Resource/Bullet/BossBullet_2.png")

        if CMonsterBullet.image[2] is None:
            CMonsterBullet.image[2] = load_image("Resource/Bullet/BossBullet_3.png")

        self.IsDead = False
        self.x, self.y = PosX, PosY
        self.speed = Speed
        self.radius = Radius
        self.angle = Angle
        self.set_dir = IsSetDir
        self.filename = FileName
        pass

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Move
        if self.set_dir:
            self.x -= math.cos(self.angle * MathMgr.PI / 180.0) * self.speed * GameFramework.frame_time
            self.y -= math.sin(self.angle * MathMgr.PI / 180.0) * self.speed * GameFramework.frame_time

        # OffSet
        if self.y >= 960 or self.y <= 0:
            self.IsDead = True

        if self.x >= 720 or self.x <= 0:
            self.IsDead = True

        return 0
        pass

    def Render(self):
        index = 0

        if self.filename == "BossBullet_1":
            index = 0
        if self.filename == "BossBullet_2":
            index = 1
        if self.filename == "BossBullet_3":
            index = 2

        if not self.IsDead:
            CMonsterBullet.image[index].draw(self.x, self.y)
        pass

    ################################

    pass