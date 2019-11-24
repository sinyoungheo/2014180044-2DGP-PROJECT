import math

PI = 3.141592


def CalcDegree(Dst, Src):
    global PI

    width = Dst.x - Src.x
    height = Dst.y - Src.y

    dist = math.sqrt(width*width + height*height)

    angle = math.acos(width / dist)

    return angle * 180.0 / PI

    pass
