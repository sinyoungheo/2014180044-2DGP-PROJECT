from pico2d import *


class CPlayer:
    def __init__(self):
        self.IsDead = False
        self.image = load_image("Resource/Player/Player01.png")
        self.frame = 0
        self.x, self.y = 360, 80

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        # 애니메이션 프레임
        self.frame = (self.frame + 1) % 4

        return 0
        pass

    def Render(self):
        self.image.clip_draw(self.frame * 128, 0, 128, 106, self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass
