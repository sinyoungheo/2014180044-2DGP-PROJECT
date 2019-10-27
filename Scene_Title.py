import GameFramework
import Scene_Stage1
from pico2d import *

image = None


def Enter():
    global image
    image = load_image("Resource/Scene/Scene_00.png")


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
