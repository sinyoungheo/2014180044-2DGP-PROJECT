from pico2d import *
import keyboard


class CPlayer:
    def __init__(self):
        self.IsDead = False
        self.image = load_image("Resource/Player/Player01.png")
        self.frame = 0
        self.x, self.y = 360, 80
        self.dir = 0
        self.speed = 10

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

        return 0
        pass

    def Render(self):
        self.image.clip_draw(self.frame * 128, 0, 128, 106, self.x, self.y)
        pass

    def DeadObject(self):
        self.IsDead = True
        pass
