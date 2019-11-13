from pico2d import *
import random
import GameFramework


class CPlayerLaser:
    image = [None, None]

    def __init__(self, Damage):
        self.IsDead = False
        self.x = random.randint(50, 700)
        self.y = 480
        self.scaleX = 128
        self.scaleY = 1024
        self.damage = Damage

        #self.index = random.randint(0, 1)

        if CPlayerLaser.image[0] is None:
            CPlayerLaser.image[0] = load_image("Resource/Effect/laser_01.png")
        if CPlayerLaser.image[1] is None:
            CPlayerLaser.image[1] = load_image("Resource/Effect/laser_02.png")
        pass

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        self.scaleX -= 600 * GameFramework.frame_time
        if self.scaleX <= 0:
            self.IsDead = True

        return 0

        pass

    def Render(self):
        index = random.randint(0, 1)

        CPlayerLaser.image[index].draw(self.x, self.y, self.scaleX, self.scaleY)
        pass

    pass
