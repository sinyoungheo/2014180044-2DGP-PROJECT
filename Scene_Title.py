from pico2d import *
import GameFramework
import Scene_Stage1

image = None
bgm = None


def Enter():
    global image
    global bgm
    image = load_image("Resource/Scene/Scene_00.png")

    bgm = load_music("Sound/dragon_flight2.mp3")
    bgm.set_volume(32)
    bgm.repeat_play()


def Exit():
    global image
    del image
    pass


def Handle_Events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.Quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.Quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                GameFramework.Change_State(Scene_Stage1)
    pass


def Update():
    pass


def Render():
    clear_canvas()

    image.draw(360, 480, 720, 960)

    update_canvas()
    pass


def Pause():
    pass


def Resume():
    pass
