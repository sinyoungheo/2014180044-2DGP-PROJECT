from pico2d import *
import GameFramework
import PlayerBullet
import ObjectMgr


class CPlayerPet:
    image = [None, None]

    def __init__(self, Target, Location, FileName):
        self.x, self.y = Target.x, Target.y
        self.target = Target
        self.location = Location
        self.filename = FileName
        # 총알 생성 주기.
        self.time_CreateBullet = 0.0
        self.time_UpdateCreateBullet = 0.5

        if CPlayerPet.image[0] is None:
            CPlayerPet.image[0] = load_image("Resource/Player/pet01.png")
        if CPlayerPet.image[1] is None:
            CPlayerPet.image[1] = load_image("Resource/Player/pet02.png")
        pass

    def Handle_Events(self):
        pass

    def Update(self):
        self.x, self.y = self.target.x - 80 * self.location, self.target.y - 20

        # 총알 생성 시간 갱신.
        self.time_CreateBullet = self.time_CreateBullet + 0.1

        if self.time_CreateBullet >= self.time_UpdateCreateBullet:
            filename = ""
            if self.filename == "pet01.png":
                filename = "pet_bullet_5.png"
            else:
                filename = "pet_bullet_3.png"

             # x, y, Damage, Radius, FileName1
            GameObject = PlayerBullet.CPlayerBullet(self.x, self.y, self.target.damage, 32, filename)
            ObjectMgr.Add_GameObject(GameObject, "PlayerBullet")

            self.time_CreateBullet = 0.0

        pass

    def Render(self):
        index = 0

        if self.filename == "pet01.png":
            index = 0
        elif self.filename == "pet02.png":
            index = 1

        CPlayerPet.image[index].draw(self.x, self.y, 64, 64)
        pass

    pass
