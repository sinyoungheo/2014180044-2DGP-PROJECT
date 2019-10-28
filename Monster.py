from pico2d import *
import random

FilePath = "Resource/Monster/"


class CMonster:
    image = None

    def __init__(self, PosX, PosY, Hp, Speed, Radius, FileName):
        global FilePath
        FilePath = FilePath + FileName

        if CMonster.image is None:
            CMonster.image = load_image(FilePath)

        self.IsDead = False
        self.frame = random.randint(0, 3)
        self.x, self.y = PosX, PosY
        self.speed = Speed
        self.radius = Radius
        self.hp = Hp
        self.max_hp = self.hp

    def Handle_Events(self):
        pass

    def Update(self):
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

        return 0
        pass

    def Render(self):
        if not self.IsDead:
            CMonster.image.clip_draw(self.frame * 76, 0, 76, 51, self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass

    pass
