from pico2d import *


class CPlayerBullet:
    image = [None]

    def __init__(self, PosX, PosY, Damage, Radius, FileName):
        if CPlayerBullet.image[0] is None:
            CPlayerBullet.image[0] = load_image("Resource/Bullet/bullet_01_01.png")

        self.IsDead = False
        self.x, self.y = PosX, PosY
        self.speed = 20
        self.damage = Damage
        self.radius = Radius
        self.filename = FileName

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
        index = 0

        if self.filename == "bullet_01_01.png":
            index = 0

        if not self.IsDead:
            CPlayerBullet.image[0].draw(self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass
