from pico2d import *
import keyboard
import PlayerBullet
import ObjectMgr


class CPlayer:
    def __init__(self):
        self.IsDead = False
        self.image = load_image("Resource/Player/Player01.png")
        self.frame = 0
        self.x, self.y = 360, 80
        self.dir = 0
        self.speed = 15
        self.radius = 64
        # 총알 생성 주기.
        self.time_CreateBullet = 0.0
        self.time_UpdateCreateBullet = 0.5
        # 경험치 및 레벨.
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        self.damage = 10
        # 탄환 이미지
        self.bullet_filename = "bullet_01_01.png"
        self.bullet_radius = 32

    def Handle_Events(self):
        if keyboard.is_pressed('left'):
            self.dir = -1
        if keyboard.is_pressed('right'):
            self.dir = 1

        events = get_events()

        for event in events:
            if event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                    self.dir = 0
                pass

        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Animation
        self.frame = (self.frame + 1) % 4

        # Move
        self.x = self.x + self.speed * self.dir

        # OffSet
        if self.x <= 0 + 64:
            self.x = self.x + self.speed
            pass
        if self.x >= 720 - 64:
            self.x = self.x - self.speed
            pass

        # Create Bullet
        self.time_CreateBullet = self.time_CreateBullet + 0.1
        if self.time_CreateBullet >= self.time_UpdateCreateBullet:
            GameObject = PlayerBullet.CPlayerBullet(self.x, self.y, self.damage, self.bullet_radius, self.bullet_filename)
            ObjectMgr.Add_GameObject(GameObject, "PlayerBullet")
            self.time_CreateBullet = 0.0

        return 0
        pass

    def Render(self):
        self.image.clip_draw(self.frame * 128, 0, 128, 106, self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass
