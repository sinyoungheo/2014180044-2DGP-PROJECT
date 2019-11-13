from pico2d import *
import GameFramework

time = 0.0


class CEffect:
    image = [None, None]

    def __init__(self, PosX, PosY, CX, CY, Speed, IsSingleEffect, IsAnimationEndDead, MaxFrame, LifeTime, ScaleX, ScaleY, FileName,
                 Time_Per_Action, Frames_Per_Action):
        self.IsDead = False
        self.x = PosX
        self.y = PosY
        self.cx = CX
        self.cy = CY
        self.speed = Speed
        self.frame = 1
        self.max_frame = MaxFrame
        self.lifetime = LifeTime
        self.scaleX = ScaleX
        self.scaleY = ScaleY
        self.filename = FileName
        self.isSingleEffect = IsSingleEffect
        self.isAnimationEndDead = IsAnimationEndDead

        self.time_per_action = Time_Per_Action
        self.action_per_time = 1.0 / self.time_per_action
        self.frames_per_action = Frames_Per_Action

        if CEffect.image[0] is None:
            CEffect.image[0] = load_image("Resource/Effect/LvUp.png")
        if CEffect.image[1] is None:
            CEffect.image[1] = load_image("Resource/Effect/dust.png")
            pass

        # if CEffect.image[1] is None:
        #     pass

    def Handle_Events(self):
        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Animation
        if not self.isSingleEffect:
            self.frame = (self.frame + self.frames_per_action * self.action_per_time * GameFramework.frame_time)
            self.frame = (self.frame + self.speed)
        if self.frame >= self.max_frame:
            if self.isAnimationEndDead:
                self.IsDead = True
            else:
                self.frame = 0

        # LifeTime
        global time
        time += 0.1
        if time >= self.lifetime:
            self.IsDead = True
            time = 0.0

        return 0
        pass

    def Render(self):
        index = 0

        if not self.IsDead:
            if self.filename == "LvUp.png":
                index = 0
            elif self.filename == "dust.png":
                index = 1

            if not self.isSingleEffect:
                CEffect.image[index].clip_draw(int(self.frame) * self.cx, 0, self.cx, self.cy, self.x, self.y, self.scaleX, self.scaleY)
            else:
                CEffect.image[index].draw(self.x, self.y, self.scaleX, self.scaleY)

        pass

    def DeadObject(self):
        self.IsDead = True
        pass

    pass
