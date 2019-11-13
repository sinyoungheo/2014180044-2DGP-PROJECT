from pico2d import *
import keyboard
import PlayerBullet
import ObjectMgr
import Effect
import GameFramework
import PlayerPet

# 자석 아이템.
bIsMagnet = False
time_magnet = 0.0
time_update_magnet = 4.0

# 탄막 강화 아이템.
bIsBulletPowerUp = False
time_bullet_power_up = 0.0
time_update_bullet_power_up = 4.0

# 새끼 용
bIsCreateFirst = False
bIsCreateSecond = False
pet_cnt = 0
pet_max_cnt = 2

# 애니메이션 프레임.
TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class CPlayer:
    def __init__(self):
        self.IsDead = False
        self.image = load_image("Resource/Player/Player01.png")
        self.frame = 0
        self.x, self.y = 360, 80
        self.dir = 0
        self.speed = 600
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
        self.bullet_filename = "bullet_Lv1.png"
        self.bullet_radius = 32
        # 코인 개수
        self.coin_cnt = 0
        # # 새끼용 생성
        # ObjectMgr.Add_GameObject(PlayerPet.CPlayerPet(self, 1, "pet01"), "PlayerPet")

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

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_1:
                    self.exp += 1000
                pass

        pass

    def Update(self):
        if self.IsDead:
            return -1

        # Animation
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * GameFramework.frame_time) % 4

        # Move
        self.x = self.x + self.speed * self.dir * GameFramework.frame_time

        # OffSet
        self.x = clamp(64, self.x, 720 - 64)
        # if self.x <= 0 + 64:
        #     self.x = self.x + self.speed
        #     pass
        # if self.x >= 720 - 64:
        #     self.x = self.x - self.speed
        #     pass

        # Level에 따른 Bullet 변경.
        self.Change_Bullet()

        # Create Bullet
        self.Create_Bullet()

        # LevelUp Check
        self.Check_LevelUp()

        # Item Magnet
        self.Item_Magnet()

        return 0
        pass

    def Render(self):
        self.image.clip_draw(int(self.frame) * 128, 0, 128, 106, self.x, self.y)
        pass

    ##################################################################################################################

    def DeadObject(self):
        self.IsDead = True
        pass

    def Check_LevelUp(self):
        # 현재 exp가 max_exp보다 작을 때 까지.
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.max_exp = self.max_exp * 1.15
            self.level += 1
            self.damage += 3

            # PosX, PosY, CX, CY, Speed, IsSingleEffect, IsAnimationEndDead, MaxFrame, LifeTime, ScaleX, ScaleY, FileName
            # time_per_action, frames_per_action
            GameObj = Effect.CEffect(self.x, self.y, 256, 256, 1, False, True, 30, 100, 256, 256, "LvUp.png", 0.8, 30)
            ObjectMgr.Add_GameObject(GameObj, "Effect")
        pass

    def Change_Bullet(self):
        if self.level >= 5:
            self.bullet_filename = "bullet_Lv2.png"
            self.bullet_radius = 32
            pass

        if self.level >= 10:
            self.bullet_filename = "bullet_Lv3.png"
            self.bullet_radius = 64
            pass

        if self.level >= 15:
            self.bullet_filename = "bullet_Lv4.png"
            self.bullet_radius = 64
            pass

        if self.level >= 20:
            self.bullet_filename = "bullet_Lv5.png"
            self.bullet_radius = 64
            pass

        if self.level >= 25:
            self.bullet_filename = "bullet_Lv6.png"
            self.bullet_radius = 50
            pass

        if self.level >= 30:
            self.bullet_filename = "bullet_Lv7.png"
            self.bullet_radius = 64
            pass

        pass

    # 자석 아이템.
    def Item_Magnet(self):
        global bIsMagnet
        global time_magnet
        global time_update_magnet

        if bIsMagnet:
            time_magnet += GameFramework.frame_time
            # print(time_magnet)
            if time_magnet >= time_update_magnet:
                time_magnet = 0.0
                bIsMagnet = False

    # 듀얼샷 아이템.
    def Create_Bullet(self):
        global bIsBulletPowerUp
        global time_bullet_power_up
        global time_update_bullet_power_up

        # 총알 생성 시간 갱신.
        self.time_CreateBullet = self.time_CreateBullet + 0.1

        if self.time_CreateBullet >= self.time_UpdateCreateBullet:
            if not bIsBulletPowerUp:
                # x, y, Damage, Radius, FileName
                GameObject = PlayerBullet.CPlayerBullet(self.x, self.y, self.damage, self.bullet_radius,
                                                        self.bullet_filename)
                ObjectMgr.Add_GameObject(GameObject, "PlayerBullet")
                self.time_CreateBullet = 0.0
            else:
                time_bullet_power_up += GameFramework.frame_time
                if time_bullet_power_up >= time_update_bullet_power_up:
                    time_bullet_power_up = 0.0
                    bIsBulletPowerUp = False

                # x, y, Damage, Radius, FileName
                GameObject = PlayerBullet.CPlayerBullet(self.x, self.y, self.damage, self.bullet_radius,
                                                        self.bullet_filename)
                ObjectMgr.Add_GameObject(GameObject, "PlayerBullet")

                # x, y, Damage, Radius, FileName
                GameObject = PlayerBullet.CPlayerBullet(self.x - 60, self.y - 20, self.damage, self.bullet_radius,
                                                        self.bullet_filename)
                ObjectMgr.Add_GameObject(GameObject, "PlayerBullet")

                # x, y, Damage, Radius, FileName
                GameObject = PlayerBullet.CPlayerBullet(self.x + 60, self.y - 20, self.damage, self.bullet_radius,
                                                        self.bullet_filename)
                ObjectMgr.Add_GameObject(GameObject, "PlayerBullet")

                self.time_CreateBullet = 0.0

        pass

    pass

    def Crate_Pet(self):
        global bIsCreateFirst
        global bIsCreateSecond
        global pet_cnt
        global pet_max_cnt

        pass
