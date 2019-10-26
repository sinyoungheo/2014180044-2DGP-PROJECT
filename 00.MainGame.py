import pico2d
import GameFramework
import Scene_Title


WINCX = 720
WINCY = 960

pico2d.open_canvas(WINCX, WINCY)

GameFramework.Run(Scene_Title)

pico2d.clear_canvas()

