from pico2d import *

IsMagnetTime = False


class CItem:
    image = [None, None, None, None]

    def __init__(self, PosX, PosY, CX, CY, Radius, ScaleX, ScaleY, Target, FileName):
        self.IsDead = False
        self.x, self.y = PosX, PosY
        self.cx, self.cy = CX, CY
        self.radius = Radius
        self.scaleX, self.scaleY = ScaleX, ScaleY
        self.target = Target
        self.filename = FileName
        self.time_Magnet = 0
        self.time_UpdateMagnet = 5

        self.speed = -6

        if CItem.image[0] is None:
            CItem.image[0] = load_image("Resource/Item/item_coin0.png")

        if CItem.image[1] is None:
            CItem.image[1] = load_image("Resource/Item/item_coin1.png")

        if CItem.image[2] is None:
            CItem.image[2] = load_image("Resource/Item/item_coin2.png")

        if CItem.image[3] is None:
            CItem.image[3] = load_image("Resource/Item/item_coin3.png")

        pass

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        self.y -= self.speed
        self.speed += 0.33

        if self.y <= 0:
            self.IsDead = True

        pass

    def Render(self):
        if self.IsDead:
            return
        index = 0

        if self.filename == "item_coin0.png":
            index = 0
        if self.filename == "item_coin1.png":
            index = 1
        if self.filename == "item_coin2.png":
            index = 2
        if self.filename == "item_coin3.png":
            index = 3

        CItem.image[index].draw(self.x, self.y, self.scaleX, self.scaleY)
        pass

    pass
