from pico2d import *
import GameFramework


class CPlayerBullet:
    image = [None, None, None, None, None, None, None]

    def __init__(self, PosX, PosY, Damage, Radius, FileName):
        if CPlayerBullet.image[0] is None:
            CPlayerBullet.image[0] = load_image("Resource/Bullet/bullet_Lv1.png")

        if CPlayerBullet.image[1] is None:
            CPlayerBullet.image[1] = load_image("Resource/Bullet/bullet_Lv2.png")

        if CPlayerBullet.image[2] is None:
            CPlayerBullet.image[2] = load_image("Resource/Bullet/bullet_Lv3.png")

        if CPlayerBullet.image[3] is None:
            CPlayerBullet.image[3] = load_image("Resource/Bullet/bullet_Lv4.png")

        if CPlayerBullet.image[4] is None:
            CPlayerBullet.image[4] = load_image("Resource/Bullet/bullet_Lv5.png")

        if CPlayerBullet.image[5] is None:
            CPlayerBullet.image[5] = load_image("Resource/Bullet/bullet_Lv6.png")

        if CPlayerBullet.image[6] is None:
            CPlayerBullet.image[6] = load_image("Resource/Bullet/bullet_Lv7.png")

        self.IsDead = False
        self.x, self.y = PosX, PosY
        self.speed = 1500
        self.damage = Damage
        self.radius = Radius
        self.filename = FileName

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Move
        self.y = self.y + self.speed * GameFramework.frame_time

        # OffSet
        if self.y >= 960:
            self.IsDead = True
            pass

        return 0
        pass

    def Render(self):
        index = 0

        if self.filename == "bullet_Lv1.png":
            index = 0
        if self.filename == "bullet_Lv2.png":
            index = 1
        if self.filename == "bullet_Lv3.png":
            index = 2
        if self.filename == "bullet_Lv4.png":
            index = 3
        if self.filename == "bullet_Lv5.png":
            index = 4
        if self.filename == "bullet_Lv6.png":
            index = 5
        if self.filename == "bullet_Lv7.png":
            index = 6

        if not self.IsDead:
            CPlayerBullet.image[index].draw(self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass
