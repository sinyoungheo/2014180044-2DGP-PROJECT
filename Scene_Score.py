from pico2d import *
import GameFramework

image = None
font = None

score = 0
flight_distance = 0


def Enter():
    global image
    image = load_image("Resource/Scene/Scene_04.png")

    global font
    font = load_font("Font/Maplestory Bold.ttf", 32)


def Exit():
    global image
    del image
    pass


def Handle_Events():
    events = get_events()

    # if keyboard.is_pressed('space'):
    #     GameFramework.Change_State(Scene_Title)

    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.Quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.Quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                # GameFramework.Change_State(Scene_Stage1)
                pass
    pass


def Update():
    global score
    pass


def Render():
    clear_canvas()

    image.draw(360, 480, 720, 960)

    global font
    global score
    global flight_distance

    font.draw(230, 460, 'C O I N        %d' % score, (255, 255, 255))
    font.draw(230, 460 - 45, 'F L I G H T  %d' % flight_distance, (255, 255, 255))
    font.draw(230, 460 - 90, 'R E S U L T  %d' % (flight_distance + score), (255, 255, 255))

    update_canvas()
    pass


def Pause():
    pass


def Resume():
    pass
