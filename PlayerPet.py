from pico2d import *
import GameFramework
import PlayerBullet


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
