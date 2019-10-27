from pico2d import *

FilePath = "Resource/Monster/"


class CMonster:
    image = None

    def __init__(self, PosX, PosY, Hp, Speed, FileName):
        global FilePath
        FileName = FilePath + FileName

        if CMonster.image is None:
            CMonster.image = load_image(FilePath)

        self.IsDead = False
        self.image = load_image("Resource/Monster/Enemy01.png")
        self.frame = 0
        self.x, self.y = PosX, PosY
        self.speed = Speed
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
        self.image.clip_draw(self.frame * 128, 0, 76, 51, self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass

    pass
