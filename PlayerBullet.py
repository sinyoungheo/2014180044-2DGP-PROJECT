from pico2d import *

FilePath = "Resource/Bullet/"


class CPlayerBullet:
    image = None

    def __init__(self, PosX, PosY, FileName):
        global FilePath
        FilePath = FilePath + FileName

        self.IsDead = False
        if CPlayerBullet.image is None:
            CPlayerBullet.image = load_image(FilePath)
        self.x, self.y = PosX, PosY
        self.speed = 20

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Move
        self.y = self.y + self.speed

        # OffSet
        if self.y >= 960:
            self.IsDead = True
            pass

        return 0
        pass

    def Render(self):
        if not self.IsDead:
            CPlayerBullet.image.draw(self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass
